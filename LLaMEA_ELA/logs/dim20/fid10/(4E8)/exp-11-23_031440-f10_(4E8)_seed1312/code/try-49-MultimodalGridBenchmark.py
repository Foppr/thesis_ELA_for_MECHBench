import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Convert to numpy array and ensure correct shape
        x = np.array(x)
        
        # Quadratic basin term - encourages convergence to origin with variable conditioning
        basin_term = 0.05 * np.sum(x**2)
        
        # Grid of global minima terms with chaotic sine wave patterns
        grid_minima = 0.0
        for i in range(self.dim):
            # Chaotic perturbations using multiple sine frequencies
            grid_minima += (np.sin(4 * np.pi * x[i]) * np.cos(3 * np.pi * x[i]) + 
                           0.5 * np.sin(7 * np.pi * x[i]) * np.cos(5 * np.pi * x[i]))
            
        # Radial symmetry component with dynamic conditioning
        radial_term = 0.0
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            radial_term = 0.3 * np.sin(10 * r) / (r + 0.1)
        
        # Enhanced sinusoidal interference terms with dynamic coupling
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling based on distance between variables
                dist = abs(x[i] - x[j])
                coupling = np.exp(-dist / (0.5 + 0.5 * np.sin(2 * np.pi * r)))
                interference += coupling * np.sin(3 * np.pi * (x[i] + x[j])) * np.cos(4 * np.pi * (x[i] - x[j]))
        
        # Add chaotic noise with multiple frequency components and amplitude modulation
        noise = 0.0
        for i in range(self.dim):
            noise += (0.1 * np.sin(15 * x[i]) * np.cos(12 * x[i]) + 
                     0.05 * np.sin(23 * x[i]) * np.cos(18 * x[i]) +
                     0.03 * np.sin(31 * x[i]))
        
        # Add a dynamic conditioning factor that varies with the dimensionality
        condition_factor = 1.0 + 0.5 * np.sin(self.dim * np.pi / 4.0)
        
        return condition_factor * (basin_term + grid_minima + radial_term + interference + noise)