import numpy as np

class MultiscaleTrigonometricValley:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base periodic trigonometric components with varying frequencies
        f = 0.0
        for i in range(self.dim):
            f += np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[i]) * np.sin(5 * x_norm[i])
            
        # Asymmetric saddle points with dynamic weights
        for i in range(self.dim):
            # Asymmetric quadratic terms with directional bias
            bias = 0.3 * np.sin(i * 0.5) + 0.2 * np.cos(i * 0.7)
            f += (x[i]**2 + bias * x[i]) * np.tanh(x[i]) + 0.2 * np.sinh(x[i]**2)
            
        # Multi-scale periodic modulations with dynamic coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                modulation = np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[j]) * np.sin(4 * x_norm[i]) * np.cos(5 * x_norm[j])
                f += 0.2 * modulation * (1 + 0.1 * np.sin(i + j) + 0.05 * np.cos(i * j))
                
        # Dynamic scaling based on proximity to critical points
        proximity = 0.0
        for i in range(self.dim):
            proximity += np.abs(x[i] - np.sin(i * 0.3)) + 0.1 * np.abs(x[i] - np.cos(i * 0.4))
        scale_factor = 1.0 + 0.5 * np.exp(-proximity / 1.0)
        f *= scale_factor
        
        # Fractal-like complexity with recursive harmonic terms
        for i in range(self.dim):
            f += 0.1 * np.sin(7 * x_norm[i]) * np.cos(11 * x_norm[i]) * np.sin(13 * x_norm[i])
            
        # Chaotic perturbations with higher frequency components
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(17 * x_norm[i]) * np.cos(19 * x_norm[i]) * np.sin(23 * x_norm[i])
        f += 0.08 * chaos
        
        # Strengthened global minimum attraction with polynomial terms
        f += 0.2 * np.sum(x**4) + 0.1 * np.sum(x**6)
        
        # Additional multi-modal structure with periodic peaks
        for i in range(self.dim):
            f += 0.15 * np.sin(8 * x[i]) * np.cos(12 * x[i]) * np.sin(16 * x[i])
            
        # Enhanced noise and irregularity with chaotic harmonic components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.03 * np.sin(29 * x_norm[i]) * np.cos(31 * x_norm[i]) + 0.02 * np.sin(37 * x_norm[i]) * np.cos(41 * x_norm[i])
        f += noise
        
        # Introduce irregular coupling between dimensions with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                dynamic_weight = 0.15 * np.sin(i * 0.2) * np.cos(j * 0.3) + 0.1 * np.sin(i * j * 0.05)
                f += dynamic_weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Add irregular fractal-like structures with recursive harmonic terms
        for i in range(self.dim):
            f += 0.03 * np.sin(13 * x_norm[i]) * np.cos(17 * x_norm[i]) * np.sin(19 * x_norm[i]) * np.cos(23 * x_norm[i])
            
        # Introduce chaotic modulation with exponential decay
        exp_mod = 0.0
        for i in range(self.dim):
            exp_mod += np.exp(-0.3 * x[i]**2) * np.sin(43 * x_norm[i]) * np.cos(47 * x_norm[i])
        f += 0.1 * exp_mod
        
        # Add multi-scale periodicity with non-uniform frequencies and amplitudes
        periodicity = 0.0
        for i in range(self.dim):
            periodicity += 0.08 * np.sin(15 * x[i]) * np.cos(20 * x[i]) * np.sin(25 * x[i])
        f += periodicity
        
        # Enhanced chaotic sensitivity with higher-order coupling terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                for k in range(j+1, min(j+3, self.dim)):
                    coupling += 0.03 * np.sin(x[i] + x[j] + x[k]) * np.cos(x[i] - x[j] + x[k])
        f += coupling
        
        return f