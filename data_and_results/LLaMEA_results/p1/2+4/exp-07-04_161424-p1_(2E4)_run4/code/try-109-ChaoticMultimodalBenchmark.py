import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence with fractional dynamics
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Precompute fractional Brownian motion noise coefficients
        self.fbm_coeffs = np.random.normal(0, 1, dim)
        
        # Precompute trigonometric coupling weights
        self.trig_weights = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractional Brownian motion inspired radial basis functions
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.logistic_seq[i])**2)
            weight = np.abs(np.sin(self.logistic_seq[i] * np.pi)) + 0.5
            rbfs[i] = weight * np.exp(-dist / (2 * 0.02**2)) * np.abs(np.sin(self.fbm_coeffs[i] * x_norm[i]))
        
        # Trigonometric coupling with chaotic phase modulation
        trig_coupling = np.sum(np.sin(self.trig_weights * x_norm + self.logistic_seq) * np.cos(2 * self.logistic_seq * x_norm))
        
        # Dynamic conditioning factor based on input magnitude
        cond_factor = 1 + 0.8 * np.sin(np.sum(x_norm**3))
        
        # Fractional polynomial interactions with chaotic coefficients
        poly_interaction = np.sum(self.logistic_seq * (x_norm**3 + 0.3 * x_norm**5 + 0.02 * x_norm**7))
        
        # Add sharp peaks using hyperbolic tangent modulation
        peaks = np.sum(np.tanh(10 * (x_norm - np.sin(self.logistic_seq)))**2)
        
        # Combine all components with dynamic weights
        total = 0.25 * np.sum(rbfs) + 0.25 * trig_coupling + 0.2 * cond_factor + 0.15 * poly_interaction + 0.15 * peaks
        
        # Add global scaling with chaotic modulation
        return total * (1 + 0.5 * np.sin(np.sum(x_norm**4) * self.logistic_seq[0]))