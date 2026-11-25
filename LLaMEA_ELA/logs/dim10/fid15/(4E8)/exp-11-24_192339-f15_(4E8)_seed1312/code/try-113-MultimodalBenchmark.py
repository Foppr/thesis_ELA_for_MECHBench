import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component
        sphere = np.sum(x**2)
        
        # Chaotic sine modulations with dynamic frequency scaling
        chaotic_mod = 0
        for i in range(self.dim):
            chaotic_mod += np.sin(7 * np.pi * x[i]) * np.cos(4 * np.pi * x[i]) * np.exp(-0.15 * np.abs(x[i]))
        
        # Radial basis functions with adaptive centers and widths
        rbf = 0
        for i in range(self.dim):
            center = 2.0 * np.sin(np.pi * i / self.dim)
            width = 0.5 + 0.5 * np.cos(np.pi * i / self.dim)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Enhanced polynomial couplings with cross-dimensional interactions
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-dimensionality
                poly_coupling += 0.3 * (x[i]**3) * (x[j]**2) * np.sin(np.pi * (x[i] + x[j]))
        
        # Quaternion-inspired cross-dimensional interactions
        quat_interaction = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                quat_interaction += 0.4 * np.sin(np.pi * (x[i]**2 + x[i+1]**2)) * np.cos(np.pi * (x[i] * x[i+1]))
        
        # Dynamic scaling and global shift
        scale_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        shift = 0.7 * np.sum(np.abs(x)**1.5)
        
        # Adaptive noise component with frequency modulation
        noise = 0.08 * np.sum(np.sin(12 * np.pi * x) ** 2 + np.cos(8 * np.pi * x) ** 2)
        
        # Combine all components
        return scale_factor * (sphere + 0.4 * chaotic_mod + 0.3 * rbf + 0.25 * poly_coupling + 0.2 * quat_interaction) + shift + noise