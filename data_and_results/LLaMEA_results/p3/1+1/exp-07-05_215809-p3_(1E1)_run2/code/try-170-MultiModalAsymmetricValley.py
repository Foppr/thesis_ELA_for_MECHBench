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
            f += 0.5 * np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[i]) + 0.3 * np.sin(5 * x_norm[i]) * np.cos(7 * x_norm[i])
            
        # Asymmetric saddle points with directional bias
        for i in range(self.dim):
            # Asymmetric quadratic with dynamic bias
            bias = 0.4 * np.sin(i * 0.8) + 0.2 * np.cos(i * 1.2)
            f += (0.5 * x[i]**2 + bias * x[i]) * np.tanh(x[i]) + 0.1 * np.sinh(x[i]**2)
            
        # Multi-scale coupling with dynamic weights - slightly modified coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                # Dynamic weight based on dimension indices - modified weights
                weight = 0.35 * np.sin(i * 0.55) * np.cos(j * 0.75) + 0.25 * np.sin(i + j * 0.35)
                f += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Fractal-like structure with recursive harmonic terms
        for i in range(self.dim):
            f += 0.2 * np.sin(11 * x_norm[i]) * np.cos(13 * x_norm[i]) * np.sin(17 * x_norm[i])
            
        # Chaotic perturbations with irregular frequency components
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(19 * x_norm[i]) * np.cos(23 * x_norm[i]) * np.sin(29 * x_norm[i]) * np.cos(31 * x_norm[i])
        f += 0.15 * chaos
        
        # Multi-modal structure with irregular peaks and valleys
        for i in range(self.dim):
            f += 0.25 * np.sin(8 * x[i]) * np.cos(12 * x[i]) * np.sin(16 * x[i])
            
        # Dynamic gradient modulation based on proximity to critical points
        proximity = 0.0
        for i in range(self.dim):
            proximity += np.abs(x[i] - np.sin(i * 0.6)) + 0.1 * np.abs(x[i] - np.cos(i * 0.4))
        scale_factor = 1.0 + 0.5 * np.exp(-proximity / 2.0)
        f *= scale_factor
        
        # Additional harmonic coupling with exponential decay - modified decay
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 0.25 * np.exp(-0.15 * (i + j)) * np.sin(i * 0.35) * np.cos(j * 0.45)
                f += weight * np.sin(2 * x[i] + 3 * x[j]) * np.cos(3 * x[i] - 2 * x[j])
                
        # Enhanced saddle point structure with irregular perturbations
        for i in range(self.dim):
            f += 0.3 * np.sin(3 * x[i]) * np.cos(4 * x[i]) * np.sin(5 * x[i]) * np.cos(6 * x[i])
            
        # Additional fractal-like complexity with nested terms
        for i in range(self.dim):
            f += 0.1 * np.sin(37 * x_norm[i]) * np.cos(41 * x_norm[i]) * np.sin(43 * x_norm[i]) * np.cos(47 * x_norm[i])
            
        # Multi-scale periodicity with non-uniform frequencies
        periodicity = 0.0
        for i in range(self.dim):
            periodicity += 0.15 * np.sin(25 * x[i]) * np.cos(30 * x[i]) * np.sin(35 * x[i])
        f += periodicity
        
        # Final scaling to ensure proper fitness landscape characteristics
        f *= 1.0 + 0.1 * np.sum(np.abs(x))
        
        # Add higher-order polynomial terms for additional curvature - modified coefficients
        f += 0.25 * np.sum(x**4) + 0.15 * np.sum(x**6)
        
        return f