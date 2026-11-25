import numpy as np

class ChaoticEllipticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced fractal elliptic factors with exponential growth
        self.elliptic_factors = np.logspace(1.0, 3.0, min(20, dim)) * 1.5
        # Dynamic saddle strengths with periodic modulation
        self.saddle_strengths = np.linspace(0.5, 6.0, min(15, dim)) * (1.0 + 0.3 * np.sin(np.arange(min(15, dim)) * 0.7))
        # Time-varying chaotic parameters with fractal scaling
        self.chaotic_params = np.random.uniform(0.2, 1.5, min(12, dim)) * (1.0 + 0.2 * np.cos(np.arange(min(12, dim)) * 0.5))
        # Hierarchical clustering with multi-fractal spacing
        self.cluster_positions = 4.0 * np.sin(np.linspace(0, 2*np.pi, min(10, dim)) * 2.5)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Fractal elliptic valley components with multi-scale curvature
        elliptic_term = 0.0
        for i in range(min(len(self.elliptic_factors), self.dim)):
            factor = self.elliptic_factors[i]
            # Multi-fractal elliptic shape with dynamic exponents
            exp1, exp2, exp3 = 2 + 0.5 * np.sin(i * 0.8), 4 + 0.3 * np.cos(i * 0.6), 6 + 0.4 * np.sin(i * 0.9)
            ellipse_val = factor * (x_norm[i] ** exp1) + 0.3 * (x_norm[i] ** exp2) + 0.05 * (x_norm[i] ** exp3)
            elliptic_term += ellipse_val
            
        # Dynamic saddle-point corridors with time-varying nonlinearity
        saddle_term = 0.0
        for i in range(min(len(self.saddle_strengths), self.dim)):
            strength = self.saddle_strengths[i]
            # Enhanced saddle with dynamic cubic and quartic modulation
            saddle_val = strength * x_norm[i] * np.sin(5.0 * x_norm[i]) + 0.15 * (x_norm[i] ** 3) + 0.05 * (x_norm[i] ** 4)
            saddle_term += saddle_val
            
        # Fractal chaotic interaction terms with nested coupling
        chaotic_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Nested fractal coupling with dynamic frequency modulation
                freq_mod = np.sin(self.chaotic_params[i % len(self.chaotic_params)] * 
                                 x_norm[j] * (i + 1) * 2.0 + np.cos(j * 0.3))
                coupling = 0.4 * (x_norm[i] ** 2) * (x_norm[j] ** 2) * freq_mod * (1.0 + 0.1 * np.sin(i * j * 0.5))
                chaotic_term += coupling
                
        # Hierarchical cluster term with fractal spacing and dynamic minima
        cluster_term = 0.0
        for i in range(self.dim):
            # Dynamic cluster positions with fractal scaling
            cluster_pos = self.cluster_positions[i % len(self.cluster_positions)]
            distance = x_norm[i] - cluster_pos
            # Multi-scale clustering with varying difficulty
            cluster_val = 1.2 * (distance ** 5) + 0.8 * (distance ** 7) + 0.3 * (distance ** 9) + 0.05 * (distance ** 11)
            cluster_term += cluster_val
            
        # Combined terms with hierarchical weights
        result = 0.9 * elliptic_term + 0.7 * saddle_term + 0.6 * chaotic_term + 0.5 * cluster_term
        
        # Add fractal dynamic noise with time-varying amplitude
        noise_amplitude = 0.05 * (1.0 + 0.1 * self.dim) * (1.0 + 0.05 * np.sin(self.dim * 0.3))
        noise = noise_amplitude * np.random.randn()
        
        return result + noise