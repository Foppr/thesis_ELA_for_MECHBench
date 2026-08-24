import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence with extreme sensitivity
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Precompute polynomial coefficients with exponential distribution
        self.poly_coeffs = np.random.exponential(1.0, dim) * np.random.choice([-1, 1], dim)
        
        # Precompute asymmetric weights for radial basis functions
        self.rb_weights = np.random.uniform(0.5, 2.0, dim)
        
        # Precompute transition thresholds
        self.thresholds = np.random.uniform(0.7, 0.95, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced radial basis function with chaotic scaling and asymmetric weights
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.logistic_seq[i])**2)
            weight = self.rb_weights[i] * np.abs(np.sin(self.logistic_seq[i] * np.pi)) + 0.3
            rbfs[i] = weight * np.exp(-dist / (2 * (0.03 + 0.02 * np.sin(self.logistic_seq[i] * 2 * np.pi))**2))
        
        # Chaotic interaction using logistic map with sine modulation and phase shifts
        chaotic = np.sum(np.sin(self.logistic_seq * x_norm + np.pi/4) * np.cos(5 * self.logistic_seq + np.pi/3))
        
        # Asymmetric noise with dynamic scaling and multi-scale components
        noise = np.sum(np.abs(x_norm) * (np.random.uniform(0.05, 1.5, self.dim) + 
                                         0.5 * np.random.uniform(0.1, 0.5, self.dim) * np.sin(x_norm * np.pi)))
        
        # Higher-order polynomial interactions with chaotic coefficients and cross-terms
        poly_interaction = np.sum(self.poly_coeffs * (x_norm**4 + 0.4 * x_norm**6 + 0.08 * x_norm**8 + 
                                                     0.1 * np.sum(x_norm**2) * x_norm**3))
        
        # Add sharp transition zones using multiple step functions with varying thresholds
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi)) > self.thresholds)
        
        # Add coupled oscillatory components for increased complexity
        oscillatory = np.sum(np.sin(x_norm * np.pi * 2) * np.cos(x_norm * np.pi * 3))
        
        # Combine all components with dynamic weights and non-linear mixing
        total = 0.2 * np.sum(rbfs) + 0.3 * chaotic + 0.15 * noise + 0.25 * poly_interaction + 0.05 * transitions + 0.1 * oscillatory
        
        # Add a global scaling factor with chaotic modulation to increase conditioning
        conditioning_factor = 1 + 0.7 * np.sin(np.sum(x_norm**2) * self.logistic_seq[0])
        return total * conditioning_factor