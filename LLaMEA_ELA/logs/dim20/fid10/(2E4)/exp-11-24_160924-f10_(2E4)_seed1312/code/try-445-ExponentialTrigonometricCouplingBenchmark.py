import numpy as np

class ExponentialTrigonometricCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize exponential decay parameters
        self.decay_rates = np.random.uniform(0.1, 2.0, dim)
        self.decay_centers = np.random.uniform(-3.0, 3.0, dim)
        # Initialize trigonometric wave components
        self.wave_amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.wave_frequencies = np.random.uniform(0.5, 4.0, dim)
        self.wave_phases = np.random.uniform(0, 2*np.pi, dim)
        # Initialize Gaussian peak parameters
        self.peak_centers = np.random.uniform(-4.0, 4.0, (dim, dim))
        self.peak_heights = np.random.uniform(1.0, 5.0, dim)
        self.peak_widths = np.random.uniform(0.5, 2.0, dim)
        # Initialize dynamic coupling weights
        self.coupling_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        np.fill_diagonal(self.coupling_weights, 0.0)
        # Time-varying parameters
        self.time_factor = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Exponential decay interactions
        for i in range(self.dim):
            decay_term = self.decay_rates[i] * np.exp(-np.abs(x[i] - self.decay_centers[i]))
            result += decay_term
            
        # Trigonometric wave interference patterns
        for i in range(self.dim):
            wave_term = self.wave_amplitudes[i] * np.sin(self.wave_frequencies[i] * x[i] + self.wave_phases[i])
            result += wave_term
            
        # Adaptive Gaussian peaks
        for i in range(self.dim):
            peak_sum = 0.0
            for j in range(self.dim):
                distance = (x[j] - self.peak_centers[i][j])**2
                peak_sum += self.peak_heights[i] * np.exp(-distance / (2 * self.peak_widths[i]**2))
            result += peak_sum
            
        # Dynamic dimensional coupling with time-varying weights
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_term = self.coupling_weights[i][j] * np.cos(x[i] * x[j])
                    coupling_sum += coupling_term * self.time_factor[i]
            result += coupling_sum
            
        # Add a global scaling factor based on dimensionality
        result *= (1.0 + 0.1 * self.dim)
        
        # Add small random noise for robustness
        result += np.random.normal(0, 0.05)
        
        return result