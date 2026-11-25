import numpy as np

class ChaoticFourierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute coefficients for Fourier series
        self.freqs = np.arange(1, 11)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Logistic map component for chaos
        logistic = 0.0
        r = 3.99  # Chaos-inducing parameter
        for i in range(100):  # Iterate to reach chaotic regime
            if i >= 90:  # Only consider last 10 iterations
                logistic += np.sin(r * x_norm[0] * (1 - x_norm[0])) if self.dim > 0 else 0.0
            x_norm[0] = r * x_norm[0] * (1 - x_norm[0]) if self.dim > 0 else 0.0
            
        # Fourier series component with varying frequencies
        fourier = np.sum(np.sin(self.freqs * x_norm) / self.freqs**2)
        
        # Add a non-smooth penalty term using absolute values and step functions
        smoothness_penalty = np.sum(np.abs(x_norm)**1.5)
        
        # Incorporate a multi-modal exponential barrier
        exp_barrier = np.sum(np.exp(-np.abs(x_norm)) * np.cos(10 * x_norm))
        
        # Combine components with dynamic weights based on input magnitude
        weight1 = 1.0 + 0.5 * np.mean(np.abs(x_norm))
        weight2 = 0.8 + 0.2 * np.std(x_norm)
        
        return weight1 * fourier + weight2 * logistic + 0.3 * smoothness_penalty + 0.2 * exp_barrier