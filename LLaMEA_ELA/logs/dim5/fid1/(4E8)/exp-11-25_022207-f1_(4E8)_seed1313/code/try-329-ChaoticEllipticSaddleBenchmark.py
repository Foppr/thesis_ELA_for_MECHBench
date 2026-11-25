import numpy as np

class ChaoticEllipticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced elliptic factors with higher variance
        self.elliptic_factors = np.logspace(0.7, 2.2, min(15, dim)) * 1.2
        # Modified saddle strengths for increased nonlinearity
        self.saddle_strengths = np.linspace(1.0, 4.0, min(12, dim)) * 1.1
        # Adjusted chaotic parameters for more complex modulation
        self.chaotic_params = np.random.uniform(0.15, 1.0, min(10, dim)) * 1.3
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Enhanced elliptic valley components with increased nonlinearity
        elliptic_term = 0.0
        for i in range(min(len(self.elliptic_factors), self.dim)):
            factor = self.elliptic_factors[i]
            # Higher-order polynomial with increased eccentricity
            ellipse_val = factor * (x_norm[i] ** 2) + 0.4 * (x_norm[i] ** 4) + 0.15 * (x_norm[i] ** 6)
            elliptic_term += ellipse_val
            
        # Modified saddle-point corridors with stronger chaotic modulation
        saddle_term = 0.0
        for i in range(min(len(self.saddle_strengths), self.dim)):
            strength = self.saddle_strengths[i]
            # Enhanced saddle with frequency doubling
            saddle_val = strength * x_norm[i] * np.sin(10.0 * x_norm[i])
            saddle_term += saddle_val
            
        # Refined chaotic interaction terms with increased coupling strength
        chaotic_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Stronger dynamic coupling with modified modulation
                modulator = np.sin(self.chaotic_params[i % len(self.chaotic_params)] * 
                                 x_norm[j] * (i + 1) * 1.5)
                coupling = 0.35 * (x_norm[i] ** 2) * (x_norm[j] ** 2) * modulator
                chaotic_term += coupling
                
        # Improved multi-scale optima clustering with shifted positions
        cluster_term = 0.0
        for i in range(self.dim):
            # Shifted cluster positions with increased separation
            cluster_pos = 3.0 * np.sin(0.6 * (i + 1) * np.pi / self.dim)
            distance = x_norm[i] - cluster_pos
            # Higher-order clustering with sharper minima
            cluster_val = 1.0 * (distance ** 4) + 0.5 * (distance ** 6) + 0.2 * (distance ** 8)
            cluster_term += cluster_val
            
        # Combined terms with adjusted weights for enhanced difficulty
        result = 0.8 * elliptic_term + 0.6 * saddle_term + 0.5 * chaotic_term + 0.4 * cluster_term
        
        # Increased dynamic noise with stronger amplitude scaling
        noise_amplitude = 0.03 * (1.0 + 0.07 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise