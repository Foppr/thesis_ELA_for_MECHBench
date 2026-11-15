import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic tent map sequence for higher frequency oscillations
        self.tent_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 2 * self.tent_seq[-1] if self.tent_seq[-1] < 0.5 else 2 * (1 - self.tent_seq[-1])
            self.tent_seq = np.append(self.tent_seq, next_val)
        self.tent_seq = self.tent_seq[:dim]
        
        # Precompute fractal-like coefficients with power-law distribution
        self.fractal_coeffs = np.random.power(2.0, dim) * 2.0 - 1.0
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal radial basis function with multi-scale chaotic weights
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            dist = np.sum((x_norm - self.tent_seq[i])**2)
            weight = np.abs(np.sin(self.tent_seq[i] * np.pi * 2)) + 0.5
            rbfs[i] = weight * np.exp(-dist / (2 * 0.02**2))
        
        # Multi-fractal chaotic interaction using tent map with cosine modulation
        chaotic = np.sum(np.cos(self.tent_seq * x_norm) * np.sin(5 * self.tent_seq))
        
        # Adaptive noise with dynamic scaling based on local curvature
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.1, 2.5, self.dim) * (1 + 0.3 * np.abs(x_norm)))
        
        # Higher-order polynomial interactions with fractal coefficients and cross-terms
        poly_interaction = np.sum(self.fractal_coeffs * (x_norm**5 + 0.3 * x_norm**7 + 0.02 * x_norm**9))
        
        # Add multiple sharp transition zones using sine wave modulation
        transitions = np.sum(np.abs(np.sin(x_norm * np.pi * 3)) > 0.8)
        
        # Combine all components with fractal weights
        total = 0.25 * np.sum(rbfs) + 0.25 * chaotic + 0.2 * noise + 0.15 * poly_interaction + 0.15 * transitions
        
        # Add a fractal scaling factor to increase conditioning
        fractal_scale = 1 + 0.8 * np.sin(np.sum(x_norm**3))
        return total * fractal_scale