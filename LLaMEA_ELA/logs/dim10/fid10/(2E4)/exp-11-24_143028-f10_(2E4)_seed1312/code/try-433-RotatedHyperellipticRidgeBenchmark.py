import numpy as np

class RotatedHyperellipticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Hyperelliptic basin parameters
        self.basin_centers = np.random.uniform(-3.0, 3.0, dim)
        self.basin_radii = np.random.uniform(0.5, 2.0, dim)
        self.exponent_params = np.random.uniform(2.0, 6.0, dim)
        # Ridge structure parameters
        self.ridge_orientations = np.random.randn(dim, dim)
        self.ridge_widths = np.random.uniform(0.1, 1.0, dim)
        self.ridge_heights = np.random.uniform(0.5, 2.5, dim)
        # Dynamic noise modulation
        self.noise_amplitude = np.random.uniform(0.1, 0.5, dim)
        self.noise_frequency = np.random.uniform(0.5, 2.0, dim)
        # Adaptive rotation matrix
        self.rotation_angles = np.random.uniform(0, 2*np.pi, dim)
        # Cross-dimensional coupling strength
        self.coupling_strength = np.random.uniform(0.1, 0.8, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply adaptive rotation
        rotated_x = np.zeros_like(x)
        for i in range(self.dim):
            rotated_x[i] = np.sum(x * np.sin(self.rotation_angles[i]) * 
                                self.ridge_orientations[i] + 
                                x * np.cos(self.rotation_angles[i]) * 
                                np.roll(self.ridge_orientations[i], 1))
        
        # Compute hyperelliptic basin terms
        fitness = 0.0
        for i in range(self.dim):
            # Basin attraction with hyperelliptic exponent
            distance = (rotated_x[i] - self.basin_centers[i]) / self.basin_radii[i]
            basin_term = np.abs(distance)**self.exponent_params[i]
            
            # Ridge structure term
            ridge_term = self.ridge_heights[i] * np.exp(-0.5 * 
                ((rotated_x[i] - self.basin_centers[i])**2) / (self.ridge_widths[i]**2))
            
            # Combine basin and ridge terms
            fitness += basin_term + ridge_term
            
        # Add cross-dimensional coupling with adaptive strength
        for i in range(self.dim):
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_factor = np.exp(-((rotated_x[i] - rotated_x[j])**2) / 
                                          (self.coupling_strength[i] * self.basin_radii[i]))
                    coupling_term += coupling_factor * (i + j)  # Weighted coupling
            fitness += coupling_term
            
        # Add dynamic noise modulation based on position and time
        noise = 0.0
        for i in range(self.dim):
            time_component = np.sin(self.noise_frequency[i] * x[i])
            noise += self.noise_amplitude[i] * time_component * (1.0 + 0.2 * np.sin(x[i]))
        
        # Normalize and add noise
        fitness = fitness / self.dim + noise
        
        return fitness