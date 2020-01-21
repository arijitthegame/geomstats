"""Manifold embedded in another manifold."""

import math

from geomstats.geometry.manifold import Manifold


class EmbeddedManifold(Manifold):
    """Class for manifolds embedded in another manifold."""

    def __init__(self, dimension, embedding_manifold):
        assert isinstance(dimension, int) or dimension == math.inf
        assert dimension > 0
        super(EmbeddedManifold, self).__init__(
            dimension=dimension)
        self.embedding_manifold = embedding_manifold

    def intrinsic_to_extrinsic_coords(self, point_intrinsic):
        """Convert from intrinsic to extrensic coordinates."""
        raise NotImplementedError(
            'intrinsic_to_extrinsic_coords is not implemented.')

    def extrinsic_to_intrinsic_coords(self, point_extrinsic):
        """Convert from extrinsic to intrensic coordinates."""
        raise NotImplementedError(
            'extrinsic_to_intrinsic_coords is not implemented.')

    def projection(self, point):
        """TODO: fill in."""
        raise NotImplementedError(
            'projection is not implemented.')

    def projection_to_tangent_space(self, vector, base_point):
        """TODO: fill in."""
        raise NotImplementedError(
            'projection_to_tangent_space is not implemented.')
