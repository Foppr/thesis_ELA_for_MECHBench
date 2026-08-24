import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence with higher sensitivity and periodicity
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1])
            self.logistic_seq = np.append(self.logistic_seq, next_val)
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Precompute polynomial coefficients for interaction terms with fractal-like distribution
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, dim)
        # Add fractal-like scaling to coefficients
        for i in range(dim):
            self.poly_coeffs[i] *= np.sin(i * np.pi / dim) + 1.5
        
        # Precompute asymmetric weights for radial basis functions
        self.rb_weights = np.random.uniform(0.5, 2.0, dim)
        
        # Precompute transition thresholds with chaotic distribution
        self.transitions = np.array([np.sin(i * np.pi / dim) * 0.5 + 0.5 for i in range(dim)])
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced radial basis function with chaotic scaling and asymmetric weights
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.logistic_seq[i])**2)
            weight = self.rb_weights[i] * np.abs(np.sin(self.logistic_seq[i] * np.pi)) + 0.5
            rbfs[i] = weight * np.exp(-dist / (2 * 0.03**2))
        
        # Chaotic interaction using logistic map with sine modulation and phase shifts
        chaotic = np.sum(np.sin(self.logistic_seq * x_norm + np.pi/4) * np.cos(5 * self.logistic_seq))
        
        # Asymmetric noise with dynamic scaling based on input magnitude and chaotic sequence
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.05, 3.0, self.dim) * (1 + 0.2 * self.logistic_seq))
        
        # Higher-order polynomial interactions with chaotic coefficients and fractal scaling
        poly_interaction = np.sum(self.poly_coeffs * (x_norm**4 + 0.4 * x_norm**6 + 0.08 * x_norm**8))
        
        # Add sharp transition zones using step functions with chaotic thresholds
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi)) > self.transitions)
        
        # Add a global scaling factor to increase conditioning with chaotic modulation
        global_scale = 1 + 0.8 * np.sin(np.sum(x_norm**2) * self.logistic_seq[0])
        
        # Combine all components with dynamic weights and chaotic modulation
        total = 0.3 * np.sum(rbfs) + 0.25 * chaotic + 0.25 * noise + 0.15 * poly_interaction + 0.05 * transitions
        
        # Add a complex harmonic modulation based on chaotic sequence
        harmonic_mod = np.sin(np.sum(x_norm * self.logistic_seq) * np.pi / 2) + 1.0
        
        return total * global_scale * harmonic_mod