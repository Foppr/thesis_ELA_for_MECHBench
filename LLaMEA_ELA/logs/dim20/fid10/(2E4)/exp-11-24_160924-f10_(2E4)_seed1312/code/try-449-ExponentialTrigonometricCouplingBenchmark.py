import numpy as np

class ExponentialTrigonometricCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize hyperbolic tangent decay parameters
        self.decay_rates = np.random.uniform(0.5, 3.0, dim)
        self.decay_centers = np.random.uniform(-4.0, 4.0, dim)
        # Initialize polynomial wave components
        self.wave_amplitudes = np.random.uniform(1.0, 4.0, dim)
        self.wave_exponents = np.random.uniform(2.0, 6.0, dim)
        self.wave_phases = np.random.uniform(0, 2*np.pi, dim)
        # Initialize dynamic Gaussian peak parameters
        self.peak_centers = np.random.uniform(-4.5, 4.5, (dim, dim))
        self.peak_heights = np.random.uniform(1.5, 6.0, dim)
        self.peak_widths = np.random.uniform(0.3, 2.5, dim)
        # Initialize asymmetric coupling weights
        self.coupling_weights = np.random.uniform(-1.5, 1.5, (dim, dim))
        np.fill_diagonal(self.coupling_weights, 0.0)
        # Frequency-modulated time-varying parameters
        self.frequency_modulators = np.random.uniform(0.8, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Hyperbolic tangent decay interactions
        for i in range(self.dim):
            decay_term = self.decay_rates[i] * np.tanh((x[i] - self.decay_centers[i])**2)
            result += decay_term
            
        # Polynomial wave interference patterns
        for i in range(self.dim):
            wave_term = self.wave_amplitudes[i] * np.sin(self.wave_exponents[i] * x[i] + self.wave_phases[i])
            result += wave_term
            
        # Dynamic Gaussian peaks with adaptive widths
        for i in range(self.dim):
            peak_sum = 0.0
            for j in range(self.dim):
                distance = (x[j] - self.peak_centers[i][j])**2
                adaptive_width = self.peak_widths[i] * (1.0 + 0.2 * np.sin(i * x[j]))
                peak_sum += self.peak_heights[i] * np.exp(-distance / (2 * adaptive_width**2))
            result += peak_sum
            
        # Asymmetric dimensional coupling with frequency-modulated weights
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_term = self.coupling_weights[i][j] * np.sin(x[i] * x[j] * self.frequency_modulators[i])
                    coupling_sum += coupling_term
            result += coupling_sum
            
        # Add a global scaling factor based on dimensionality with non-linear component
        result *= (1.0 + 0.2 * self.dim + 0.05 * np.sin(self.dim))
        
        # Add small random noise for robustness
        result += np.random.normal(0, 0.03)
        
        return result