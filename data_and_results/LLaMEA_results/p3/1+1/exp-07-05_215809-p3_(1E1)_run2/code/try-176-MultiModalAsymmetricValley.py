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
            
        # Multi-scale coupling with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                # Dynamic weight based on dimension indices
                weight = 0.3 * np.sin(i * 0.5) * np.cos(j * 0.7) + 0.2 * np.sin(i + j * 0.3)
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
        
        # Additional harmonic coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 0.2 * np.exp(-0.1 * (i + j)) * np.sin(i * 0.3) * np.cos(j * 0.4)
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
        
        # Add higher-order polynomial terms for additional curvature
        f += 0.2 * np.sum(x**4) + 0.1 * np.sum(x**6)
        
        # Introduce stronger chaotic and irregular components
        irregularity = 0.0
        for i in range(self.dim):
            irregularity += 0.3 * np.sin(47 * x[i]) * np.cos(53 * x[i]) * np.sin(59 * x[i]) * np.cos(61 * x[i])
        f += 0.2 * irregularity
        
        # Add multi-scale chaotic coupling with non-linear modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                weight = 0.25 * np.sin(i * 0.4) * np.cos(j * 0.6) * np.sin((i+j) * 0.2)
                f += weight * np.sin(3 * x[i] + 2 * x[j]) * np.cos(2 * x[i] - 3 * x[j]) * np.tanh(x[i]**2 + x[j]**2)
                
        # Enhanced multi-modal structure with nested peaks
        for i in range(self.dim):
            f += 0.3 * np.sin(10 * x[i]) * np.cos(15 * x[i]) * np.sin(20 * x[i]) * np.cos(25 * x[i])
            
        # Introduce dynamic scaling based on global landscape features
        global_scale = 1.0 + 0.3 * np.sin(np.sum(x**2) * 0.1) * np.cos(np.sum(x) * 0.05)
        f *= global_scale
        
        # Add irregular fractal-like coupling between dimensions
        fractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                fractal_coupling += 0.15 * np.sin(7 * x[i] + 9 * x[j]) * np.cos(11 * x[i] - 13 * x[j]) * np.sin(17 * x[i] + 19 * x[j])
        f += fractal_coupling
        
        # Final non-linear transformation to increase complexity
        f = f * (1.0 + 0.05 * np.sin(np.sum(x**3) * 0.01))
        
        return f