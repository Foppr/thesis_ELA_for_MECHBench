import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        quadratic = np.sum(x**2) / self.dim
        
        # Asymmetric hyperbolic sine interaction terms with variable coefficients
        sinh_interaction = 0.0
        for i in range(self.dim):
            sinh_interaction += np.sinh(2.0 * x[i]) ** 3
        
        # Exponentially decaying correlation structure with dynamic decay rates
        decay_corr = 0.0
        for i in range(self.dim - 1):
            decay_rate = 0.15 * (1.0 + 0.5 * np.sin(0.5 * i))
            decay_corr += np.exp(-decay_rate * (i + 1)) * (x[i] - x[i+1])**2
        
        # Chaotic saddle-point component with multiple unstable fixed points and dynamic scaling
        chaotic_saddle = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(0.7 * i)
            chaotic_saddle += scale_factor * np.sin(23 * x[i]) * np.cos(29 * x[i]) * np.tanh(x[i])
        
        # Asymmetric cubic interaction terms with phase shifts
        asym_cubic = 0.0
        for i in range(self.dim - 2):
            phase_shift = 0.5 * np.cos(0.3 * i)
            asym_cubic += (x[i] ** 3) * (x[i+1] ** 2) * (1.0 + phase_shift)
        
        # Rugged terrain with multiple local minima using high-frequency cosine and sine combinations
        rugged = 0.0
        for i in range(self.dim):
            rugged += np.cos(60 * x[i]) ** 2 + 0.5 * np.sin(40 * x[i]) ** 2
        
        # Higher-order polynomial interactions with cross-terms
        poly_interaction = 0.0
        for i in range(self.dim - 3):
            poly_interaction += (x[i] ** 4) * (x[i+1] ** 3) * (x[i+2] ** 2)
        
        # Dynamically shifted global minimum to increase optimization difficulty
        shift_term = 0.0
        for i in range(self.dim):
            shift_term += np.sin(0.5 * x[i]) * np.cos(0.3 * x[i]) * (i + 1)
        
        # Combine all terms to create a complex landscape
        return quadratic + 0.3 * sinh_interaction + 0.2 * decay_corr + 0.25 * chaotic_saddle + 0.15 * asym_cubic + 0.35 * rugged + 0.1 * poly_interaction + 0.2 * shift_term