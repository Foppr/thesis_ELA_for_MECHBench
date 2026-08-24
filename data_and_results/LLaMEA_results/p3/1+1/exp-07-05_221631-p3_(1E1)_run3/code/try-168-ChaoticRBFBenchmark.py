import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize random centers for radial basis functions
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        # Random weights for each RBF
        self.weights = np.random.uniform(-2.0, 2.0, 10)
        # Chaotic phase shifts using logistic map
        self.chaos_seed = 0.5
        self.chaos_rate = 3.9
        # Adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 10.0, dim)
        # Control the number of RBFs used
        self.num_rbf = min(10, dim * 2)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply adaptive conditioning
        x_conditioned = x * self.conditioning_factors
        
        # Compute chaotic phase shift
        chaos_phase = self.chaos_seed
        for _ in range(self.dim):
            chaos_phase = self.chaos_rate * chaos_phase * (1 - chaos_phase)
        chaos_shift = chaos_phase * 0.5
        
        # Evaluate radial basis functions
        f_val = 0.0
        for i in range(self.num_rbf):
            center = self.centers[i]
            diff = x_conditioned - center
            distance_sq = np.sum(diff**2)
            # RBF with Gaussian shape
            rbf_val = self.weights[i] * np.exp(-distance_sq / (2 * (0.5 + i * 0.1)**2))
            f_val += rbf_val
            
        # Add chaotic modulation to the result
        f_val *= (1 + 0.3 * np.sin(chaos_shift * np.sum(x_conditioned)))
        
        # Add a quadratic penalty term to encourage convergence to the global minimum
        f_val += 0.01 * np.sum(x_conditioned**2)
        
        # Add a sinusoidal modulation to increase complexity
        sin_mod = np.sin(0.5 * np.sum(x_conditioned))
        f_val += 0.2 * sin_mod
        
        return f_val