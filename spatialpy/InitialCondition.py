import numpy


class InitialCondition():
    """ Class used to defined initial conditions in SpatialPy.
        SubClasses must implement the 'apply(model)' method, which 
        direction modifies the model.u0[species,voxel] matrix.
    """

    def apply(self, model):
        raise ModelError("spatialpy.InitialCondition subclasses must implement apply()")


class ScatterInitialCondition(InitialCondition):
    
    def __init__(self, species, count, subdomains=None):
        """ Scatter 'count' of 'species' randomly over the list of subdomains
            (all subdomains if None)."""
        self.species = species
        self.count = count
        self.subdomains = subdomains

    def apply(self, model):

        spec_name = self.species.name
        for spec_ndx in range(len(model.listOfSpecies)):
            if model.listOfSpecies[spec_ndx] = self.species: break

        if self.subdomains is None:
            nvox = model.mesh.get_num_voxels()
            for mol in range(self.count):
                vtx = numpy.random.randint(0, nvox)
                self.u0[spec_ndx, vtx] += 1
        else:
            allowed_voxels = []
            for i in range(model.mesh.get_num_voxels()):
                if model.sd[i] in self.subdomains:
                    allowed_voxels.append(i)
            nvox = len(alowed_voxels)
            if nvox==0: raise ModelError("ScatterInitialCondition has zero voxels to scatter in")
            for mol in range(self.count):
                v_ndx = numpy.random.randint(0, nvox)
                vtx = allowed_voxels[v_ndx]
                self.u0[spec_ndx, vtx] += 1

