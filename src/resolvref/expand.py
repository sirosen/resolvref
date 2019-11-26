#!/usr/bin/env python

import collections
import functools

from resolvref.exceptions import RecursiveExpansionForbiddenError


def _is_ref(item):
    return isinstance(item, dict) and "$ref" in item


def _ref_is_internal(item):
    return item["$ref"].startswith("#/")


class Resolver:
    def __init__(self, document, cachefunc=None, allow_recursive=True):
        if cachefunc is None:
            cachefunc = functools.lru_cache(1024)

        self.document = document
        self.allow_recursive = allow_recursive
        self._recursion_detector = set()
        self._cached_read_internal_ref = cachefunc(self._read_internal_refpath)

    def _check_recursive(self, data):
        if self.allow_recursive:
            return True
        else:
            dataid = id(data)
            if dataid in self._recursion_detector:
                raise RecursiveExpansionForbiddenError(
                    "recursion detected with allow_recursive=False"
                )
            else:
                self._recursion_detector.add(dataid)

    def _read_internal_refpath(self, refpath):
        refpath = refpath.split("/")[1:]
        cur = self.document
        for step in refpath:
            cur = cur[step]
        self._check_recursive(cur)
        return self._resolve_references(cur)

    def _resolve_references(self, data):
        if _is_ref(data):
            if _ref_is_internal(data):
                return self._cached_read_internal_ref(data["$ref"])
            else:
                raise NotImplementedError("External references not yet supported.")

        if isinstance(data, dict):
            return collections.OrderedDict(
                [(k, self._resolve_references(v)) for (k, v) in data.items()]
            )
        elif isinstance(data, list):
            return [self._resolve_references(v) for v in data]
        else:
            return data

    def resolve_references(self):
        return self._resolve_references(self.document)


def resolve_references(data, resolver=None, allow_recursive=True):
    resolver = Resolver(data, allow_recursive=allow_recursive)
    return resolver.resolve_references()
