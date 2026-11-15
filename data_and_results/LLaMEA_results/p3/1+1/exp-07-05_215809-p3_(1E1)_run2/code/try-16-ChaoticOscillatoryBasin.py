import numpy as np

class ChaoticOscillatoryBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base chaotic oscillator component with logistic map influence
        f = 0.0
        for i in range(self.dim):
            # Logistic-like term with varying parameter
            r = 3.8 + 0.2 * np.sin(i)
            logistic = r * np.sin(x_norm[i]) * (1 - np.sin(x_norm[i])**2)
            f += logistic**2
            
        # Phase-coupled harmonic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling strength varies with dimension index
                coupling_strength = 0.5 * (1 + np.sin(i * 0.3) * np.cos(j * 0.3))
                phase_diff = x_norm[i] - x_norm[j]
                f += coupling_strength * np.sin(3 * phase_diff) * np.cos(2 * phase_diff)
                
        # Fractal-like basin structure with recursive sine components
        for i in range(self.dim):
            # Recursive fractal term with decreasing amplitude
            fractal_sum = 0.0
            for k in range(1, 6):
                fractal_sum += (0.3**k) * np.sin(2**k * x_norm[i])
            f += fractal_sum**2
            
        # Multi-scale chaotic modulation
        modulator = 1.0
        for i in range(self.dim):
            modulator *= np.sin(x_norm[i] * 0.5 + 0.1 * i) + 1.5
        f *= modulator
        
        # Saddle point enhancement with hyperbolic tangent
        for i in range(self.dim):
            f += 0.2 * np.tanh(x[i]) * (x[i]**2 + 1)
            
        # Asymmetric basin distortion
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += 0.1 * np.sin(x[i] * 1.2) * np.cos(x[i] * 0.8)
        f += asymmetry**2
        
        # Global minimum attraction with higher-order polynomial
        f += 0.1 * np.sum(x**6)
        
        # Chaotic noise perturbation
        noise = 0.03 * np.sum(np.sin(7 * x_norm) + np.cos(11 * x_norm))
        f += noise
        
        return f