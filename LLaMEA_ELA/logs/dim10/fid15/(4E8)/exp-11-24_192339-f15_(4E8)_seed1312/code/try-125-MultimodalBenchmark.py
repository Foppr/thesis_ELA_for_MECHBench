import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component
        sphere = np.sum(x**2)
        
        # Chaotic sine modulation with dynamic frequency and amplitude
        chaotic_mod = 0
        for i in range(self.dim):
            freq = 2.5 + 1.5 * np.sin(0.6 * x[i])
            amp = 1.2 + 0.3 * np.cos(0.4 * x[i])
            chaotic_mod += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 3.0)
        
        # Radial basis function with multi-scale Gaussian components
        rbf = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced interaction
                dist = np.abs(x[i] - x[j])
                rbf += np.exp(-0.5 * (dist / (0.7 + np.abs(x[i]) + np.abs(x[j])))**2) * np.sin(3 * np.pi * dist)
        
        # Enhanced polynomial couplings with cross-dimensional interactions
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**4 + x[j]**4) * np.sin(0.3 * (x[i] + x[j]))
        
        # Quaternion-inspired cross-dimensional interactions
        quat_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i < self.dim and j < self.dim:
                    term = np.sin(0.3 * (x[i]**2 + x[j]**2)) * np.cos(0.4 * (x[i] - x[j]))
                    quat_interaction += term
        
        # Exponential decay with dynamic scaling
        exp_decay = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_decay += 0.15 * np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(2 * np.pi * (x[i] + x[j]))
        
        # Adaptive noise component
        noise = 0.04 * np.sum(np.sin(7 * np.pi * x) ** 2)
        
        # Global shift and scaling factor
        shift = 0.25 * np.sum(np.abs(x))
        scale_factor = 1.0 + 0.35 * np.log(self.dim + 1)
        
        # Combine all components with optimized weights
        return scale_factor * (sphere + 0.35 * chaotic_mod + 0.3 * rbf + 0.25 * poly_coupling + 
                              0.2 * quat_interaction + 0.15 * exp_decay) + shift + noise