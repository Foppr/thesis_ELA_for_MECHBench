import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos component with varying exponents
        poly_chaos = np.sum(x_norm**6 + 0.7 * x_norm**5 + 0.3 * x_norm**4 + 0.1 * x_norm**3)
        
        # Saddle point inducing term with hyperbolic tangent
        saddle = np.sum(np.tanh(5 * x_norm) * np.tanh(3 * x_norm**2))
        
        # Sinusoidal modulation with dimensionally adaptive frequencies
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 10 + 5 * np.sin(i * np.pi / self.dim)
            sin_mod += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Chaotic coupling between dimensions using logistic map-like interactions
        chaotic_coupling = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic_coupling += np.sin(20 * x_norm[i] * x_norm[i+1]) * np.cos(15 * x_norm[i] * x_norm[i+1])
        
        # High-order polynomial cross-terms with exponential scaling
        cross_terms = 0.0
        if self.dim > 2:
            for i in range(self.dim - 2):
                cross_terms += np.exp(-x_norm[i]**2) * x_norm[i+1]**3 * x_norm[i+2]**2
                
        # Asymmetric exponential decay with varying scale parameters
        asym_exp = np.sum(0.5 * np.exp(-2 * np.abs(x_norm)) + 0.3 * np.exp(-3 * np.abs(x_norm)**1.5))
        
        # Multi-scale trigonometric polynomial with varying amplitudes
        trig_poly = 0.0
        for i in range(self.dim):
            trig_poly += (np.sin(12 * x_norm[i])**2 + 0.5 * np.cos(18 * x_norm[i])**2 + 
                         0.3 * np.sin(24 * x_norm[i]) * np.cos(30 * x_norm[i]))
        
        # Dimensionality-dependent weight adjustment
        dim_weight = 1.0 + 0.05 * (self.dim - 1)
        
        # Add noise for robustness
        noise = 0.001 * np.random.random()
        
        # Combine all components
        return (0.3 * poly_chaos * dim_weight + 
                0.25 * saddle * dim_weight + 
                0.2 * sin_mod * dim_weight + 
                0.15 * chaotic_coupling * dim_weight + 
                0.1 * cross_terms * dim_weight + 
                0.1 * asym_exp * dim_weight + 
                0.05 * trig_poly * dim_weight + 
                noise)