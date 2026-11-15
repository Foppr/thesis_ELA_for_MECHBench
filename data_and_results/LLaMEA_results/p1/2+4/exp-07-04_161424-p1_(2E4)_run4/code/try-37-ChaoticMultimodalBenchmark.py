import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence with higher sensitivity
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 15):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced radial basis functions with asymmetric width and shifted centers
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            diff = x_norm - (self.logistic_seq[i] + 0.1 * np.sin(self.logistic_seq[i] * 10))
            rbfs[i] = np.exp(-np.sum(diff**2) / (2 * (0.05 + 0.1 * np.abs(self.logistic_seq[i])**2)))
        
        # Chaotic dynamics with higher frequency modulation
        chaotic = np.sum(np.sin(self.logistic_seq * (2 * np.pi * x_norm + np.pi/4)) * 
                        np.exp(-np.abs(self.logistic_seq)))
        
        # Heavy-tailed asymmetric noise with dynamic scaling
        noise = np.sum(np.abs(x_norm)**1.5 * np.random.lognormal(0, 0.5, self.dim))
        
        # Higher-order polynomial interactions with cross-terms
        poly_interaction = (np.sum(x_norm**4) + 
                          0.3 * np.sum(x_norm**6) + 
                          0.05 * np.sum(x_norm**8) + 
                          0.2 * np.sum(x_norm[:-1] * x_norm[1:]))
        
        # Add a global scaling factor that varies with dimension
        global_scale = 1.0 + 0.5 * np.sin(self.dim * 0.1)
        
        # Combine all components with non-linear weighting
        return global_scale * (0.25 * np.sum(rbfs) + 
                              0.35 * chaotic + 
                              0.25 * noise + 
                              0.15 * poly_interaction)