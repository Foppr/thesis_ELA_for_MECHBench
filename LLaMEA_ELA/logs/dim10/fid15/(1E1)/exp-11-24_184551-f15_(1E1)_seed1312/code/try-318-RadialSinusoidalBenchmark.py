import numpy as np

class RadialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Center minimum
        center_min = 0.0
        
        # Radial sinusoidal wells
        radial_distance = np.sqrt(np.sum(x**2))
        
        # Create multiple sinusoidal wells around the origin
        num_wells = max(3, self.dim)
        well_depths = np.linspace(1.0, 5.0, num_wells)
        well_angles = np.linspace(0, 2*np.pi, num_wells, endpoint=False)
        
        # Calculate contributions from each well
        total_contribution = 0.0
        for i in range(num_wells):
            angle = well_angles[i]
            # Position of the well in 2D
            well_x = 3.0 * np.cos(angle)
            well_y = 3.0 * np.sin(angle)
            
            # Distance from current point to well
            dist_to_well = np.sqrt((x[0] - well_x)**2 + (x[1] - well_y)**2)
            
            # Sinusoidal contribution with exponential decay
            contribution = well_depths[i] * np.exp(-dist_to_well) * np.sin(dist_to_well)
            total_contribution += contribution
            
        # Add quadratic basin term for global convergence
        basin_term = 0.1 * radial_distance**2
        
        # Add noise for non-triviality
        noise = 0.05 * np.sum(np.sin(x))
        
        return basin_term - total_contribution + noise