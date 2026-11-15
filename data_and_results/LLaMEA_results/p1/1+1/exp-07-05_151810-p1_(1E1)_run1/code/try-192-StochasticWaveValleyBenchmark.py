import numpy as np

class StochasticWaveValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with multi-dimensional interaction
        exp_component = np.sum(0.8 * np.exp(-0.5 * np.sum((x - 1.0)**2)) * np.exp(-0.3 * np.sum((x + 1.0)**2)))
        
        # Trigonometric wave interference with varying frequencies and amplitudes
        wave = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.3 * i)
            amp = 1.0 + 0.3 * np.cos(0.4 * i)
            wave += amp * np.sin(freq * x[i] + 0.2 * np.sin(0.5 * x[i])) * np.cos(freq * x[i] + 0.1 * np.cos(0.3 * x[i]))
        
        # Stochastic perturbation with adaptive amplitude scaling
        stochastic = 0.0
        for i in range(self.dim):
            # Adaptive amplitude based on position
            amp_stoch = 0.5 * (1.0 + np.sin(0.2 * x[i]))
            # Random perturbation with position-dependent variance
            variance = 0.1 + 0.05 * np.abs(x[i])
            stochastic += amp_stoch * np.random.normal(0.0, variance)
        
        # Multi-scale radial component with oscillating modulation
        radial = np.sum(0.6 * np.exp(-0.2 * np.sum(x**2)) * (1.0 + 0.4 * np.sin(2.0 * np.sum(x)) + 0.3 * np.cos(0.5 * np.sum(x))))
        
        # Cross-term interaction with asymmetric coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.3 * np.sin(0.5 * x[i]) * np.cos(0.4 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Combine all components with dynamic weighting
        weight_exp = 1.0 + 0.2 * np.sin(0.1 * np.sum(x))
        weight_wave = 1.0 + 0.15 * np.cos(0.2 * np.sum(x))
        weight_stoch = 1.0 + 0.1 * np.sin(0.25 * np.sum(x))
        weight_radial = 1.0 + 0.1 * np.cos(0.3 * np.sum(x))
        weight_cross = 1.0 + 0.05 * np.sin(0.4 * np.sum(x))
        
        result = weight_exp * exp_component + weight_wave * wave + weight_stoch * stochastic + weight_radial * radial + weight_cross * cross_term
        
        return result