import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component
        sphere = np.sum(x**2)
        
        # Intensified chaotic sine modulation with dynamic frequency and amplitude
        chaotic_mod = 0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.7 * x[i])
            amp = 1.5 + 0.5 * np.cos(0.5 * x[i])
            chaotic_mod += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Augmented radial basis function with multi-scale Gaussian components
        rbf = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction
                dist = np.abs(x[i] - x[j])
                rbf += np.exp(-0.5 * (dist / (0.5 + np.abs(x[i]) + np.abs(x[j])))**2) * np.sin(4 * np.pi * dist)
        
        # Enhanced polynomial couplings with cross-dimensional interactions
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**5 + x[j]**5) * np.sin(0.4 * (x[i] + x[j]))
        
        # Enhanced quaternion-inspired cross-dimensional interactions
        quat_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i < self.dim and j < self.dim:
                    term = np.sin(0.4 * (x[i]**2 + x[j]**2)) * np.cos(0.5 * (x[i] - x[j]))
                    quat_interaction += term
        
        # Exponential decay with dynamic scaling
        exp_decay = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_decay += 0.2 * np.exp(-0.4 * (x[i] - x[j])**2) * np.sin(3 * np.pi * (x[i] + x[j]))
        
        # Enhanced noise component
        noise = 0.08 * np.sum(np.sin(9 * np.pi * x) ** 2)
        
        # Global shift and scaling factor
        shift = 0.3 * np.sum(np.abs(x))
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combine all components with optimized weights
        return scale_factor * (sphere + 0.4 * chaotic_mod + 0.35 * rbf + 0.3 * poly_coupling + 
                              0.25 * quat_interaction + 0.2 * exp_decay) + shift + noise