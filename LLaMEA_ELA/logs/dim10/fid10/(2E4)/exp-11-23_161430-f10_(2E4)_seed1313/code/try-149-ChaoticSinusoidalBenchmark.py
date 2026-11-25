import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameter generation for each dimension
        self.chaos_params = 1.0 + 2.0 * np.sin(np.arange(dim) * 1.7 + np.pi/5)
        self.freq_modulators = 3.0 + 2.0 * np.cos(np.arange(dim) * 1.2 + np.pi/3)
        self.amplitude_modulators = 2.0 + 1.5 * np.sin(np.arange(dim) * 1.9 + np.pi/7)
        self.decay_rates = 0.5 + 1.0 * np.cos(np.arange(dim) * 1.4 + np.pi/4)
        # Cross-dimensional coupling coefficients (slightly modified)
        self.coupling_strengths = 1.5 + 0.6 * np.sin(np.arange(dim) * 1.1 + np.pi/6)
        
    def f(self, x):
        # Ensure input is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Main chaotic sinusoidal component with variable frequencies
        main_term = 0.0
        for i in range(self.dim):
            freq = self.freq_modulators[i]
            amp = self.amplitude_modulators[i]
            main_term += amp * np.sin(freq * x[i] + self.chaos_params[i]) * \
                         np.cos(freq * x[i]**2 + 0.5 * np.sin(x[i]))
        
        # Exponential decay interaction between dimensions (modified coupling)
        decay_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.coupling_strengths[i] * self.coupling_strengths[j]
                distance = np.abs(x[i] - x[j])
                decay_interaction += coupling * np.exp(-self.decay_rates[i] * distance) * \
                                    np.sin(2.0 * x[i] + 1.5 * x[j] + 0.3 * np.cos(x[i]))
        
        # High-order polynomial with chaotic perturbations (modified exponents)
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i]**9 - 2*x[i]**6 + x[i]**4 - 0.5*x[i]) * \
                         np.exp(-0.2 * x[i]**2 + 0.1 * np.sin(x[i]) + 0.05 * np.cos(x[i]))
        
        # Saddle-point like structure with sinusoidal modulation
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x[i]**4 - 6*x[i]**2 + 9) * \
                           np.sin(0.8 * x[i] + self.chaos_params[i]) * \
                           np.cos(0.3 * x[i]**2)
        
        # Cross-dimensional chaotic coupling with exponential decay (modified interaction)
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 3) % self.dim
            cross_coupling += np.exp(-0.5 * (x[i] - x[j])**2) * \
                              np.sin(3.0 * x[i] + 2.0 * x[k] + 0.4 * np.cos(x[i])) * \
                              np.cos(1.5 * x[j] + 0.6 * np.sin(x[k]))
        
        # Combine all components
        result = 0.25 * np.sum(x**2) + 0.3 * main_term + 0.15 * decay_interaction + \
                 0.12 * poly_term + 0.1 * saddle_term + 0.05 * cross_coupling
        
        return result