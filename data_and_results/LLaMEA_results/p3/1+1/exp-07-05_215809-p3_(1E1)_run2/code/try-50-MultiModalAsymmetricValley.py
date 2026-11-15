import numpy as np

class MultiModalAsymmetricValley:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base periodic component with varying frequencies and amplitudes
        f = 0.0
        for i in range(self.dim):
            f += np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[i]) * np.sin(5 * x_norm[i])
            
        # Asymmetric saddle points with dimension-specific weights
        for i in range(self.dim):
            # Add asymmetric quadratic and cubic terms
            weight = 0.5 + 0.5 * np.sin(i * 0.3)
            f += weight * (x[i]**2 + 0.3 * x[i]**3) * np.tanh(x[i])
            
        # Multi-scale periodic modulations with dynamic coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = np.sin(x[i]) * np.cos(x[j]) * np.sin(0.5 * (x[i] + x[j]))
                f += 0.2 * coupling * (1 + 0.1 * np.sin(i * j))
                
        # Dynamic scaling based on distance from reference points
        scale_factor = 1.0
        for i in range(self.dim):
            dist = np.abs(x[i] - np.sin(i * 0.4)) + np.abs(x[i] - np.cos(i * 0.3))
            scale_factor *= (1.0 + 0.5 * np.exp(-dist))
        f *= scale_factor
        
        # Fractal-like structure with recursive harmonic components
        for i in range(self.dim):
            f += 0.1 * np.sin(7 * x_norm[i]) * np.cos(11 * x_norm[i]) * np.sin(13 * x_norm[i]) * np.cos(17 * x_norm[i])
            
        # Add chaotic perturbations with varying amplitudes
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(19 * x_norm[i]) * np.cos(23 * x_norm[i]) * np.sin(29 * x_norm[i])
        f += 0.05 * chaos
        
        # Strengthened global minimum attraction with polynomial terms
        f += 0.2 * np.sum(x**4) + 0.1 * np.sum(x**6)
        
        # Additional multi-modal structure with irregular peaks
        for i in range(self.dim):
            f += 0.15 * np.sin(8 * x[i]) * np.cos(12 * x[i]) * np.sin(16 * x[i])
            
        # Irregular coupling between dimensions with varying weights
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 0.3 * np.sin(i * 0.2) * np.cos(j * 0.3) + 0.2 * np.sin(i * j * 0.1)
                f += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Add irregular fractal-like structures
        for i in range(self.dim):
            f += 0.08 * np.sin(31 * x_norm[i]) * np.cos(37 * x_norm[i]) * np.sin(41 * x_norm[i])
            
        # Introduce dynamic sensitivity with exponential terms
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += np.exp(-0.3 * x[i]**2) * np.sin(43 * x_norm[i])
        f += 0.1 * exp_term
        
        # Add multi-scale periodicity with non-uniform frequencies
        periodicity = 0.0
        for i in range(self.dim):
            periodicity += 0.1 * np.sin(15 * x[i]) * np.cos(20 * x[i])
        f += periodicity
        
        # Enhanced coupling with higher-order terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                for k in range(j+1, min(j+3, self.dim)):
                    coupling += 0.03 * np.sin(x[i] + x[j] + x[k])
        f += coupling
        
        return f