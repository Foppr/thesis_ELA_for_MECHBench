import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameter generation for each dimension
        self.chaos_params = 2.0 + 3.0 * np.sin(np.arange(dim) * 2.1 + np.pi/4)
        self.freq_modulators = 4.0 + 3.0 * np.cos(np.arange(dim) * 1.8 + np.pi/5)
        self.amplitude_modulators = 3.0 + 2.0 * np.sin(np.arange(dim) * 2.3 + np.pi/8)
        self.decay_rates = 0.8 + 1.5 * np.cos(np.arange(dim) * 1.6 + np.pi/3)
        # Enhanced cross-dimensional coupling coefficients
        self.coupling_strengths = 1.5 + 1.2 * np.sin(np.arange(dim) * 1.3 + np.pi/7)
        
    def f(self, x):
        # Ensure input is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Main chaotic sinusoidal component with variable frequencies and enhanced modulations
        main_term = 0.0
        for i in range(self.dim):
            freq = self.freq_modulators[i]
            amp = self.amplitude_modulators[i]
            main_term += amp * np.sin(freq * x[i] + self.chaos_params[i]) * \
                         np.cos(freq * x[i]**2 + 0.7 * np.sin(x[i]) + 0.3 * np.cos(x[i]**2))
        
        # Enhanced exponential decay interaction between dimensions
        decay_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.coupling_strengths[i] * self.coupling_strengths[j]
                distance = np.abs(x[i] - x[j])
                decay_interaction += coupling * np.exp(-self.decay_rates[i] * distance**1.5) * \
                                    np.sin(2.5 * x[i] + 1.8 * x[j] + 0.4 * np.cos(x[i]) + 0.2 * np.sin(x[j]))
        
        # Higher-order polynomial with enhanced chaotic perturbations
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i]**9 - 3*x[i]**7 + 3*x[i]**5 - x[i]**3 - 0.7*x[i]) * \
                         np.exp(-0.3 * x[i]**2 + 0.15 * np.sin(x[i]) + 0.08 * np.cos(x[i]) + 0.05 * np.sin(x[i]**2))
        
        # Enhanced saddle-point like structure with sinusoidal modulation
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x[i]**5 - 10*x[i]**3 + 25*x[i]) * \
                           np.sin(1.0 * x[i] + self.chaos_params[i]) * \
                           np.cos(0.4 * x[i]**2 + 0.2 * np.sin(x[i]))
        
        # Enhanced cross-dimensional chaotic coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 4) % self.dim
            cross_coupling += np.exp(-0.7 * (x[i] - x[j])**2) * \
                              np.sin(3.5 * x[i] + 2.5 * x[k] + 0.5 * np.cos(x[i]) + 0.3 * np.sin(x[k])) * \
                              np.cos(1.8 * x[j] + 0.7 * np.sin(x[k]) + 0.4 * np.cos(x[j]))
        
        # Additional chaotic cross-dimensional interaction
        additional_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+2, self.dim):
                additional_coupling += np.exp(-0.3 * (x[i] - x[j])**3) * \
                                       np.sin(1.5 * x[i] + 1.2 * x[j] + 0.2 * np.cos(x[i]**2)) * \
                                       np.cos(0.9 * x[i] + 0.6 * x[j] + 0.1 * np.sin(x[j]**2))
        
        # Combine all components
        result = 0.3 * np.sum(x**2) + 0.4 * main_term + 0.2 * decay_interaction + \
                 0.15 * poly_term + 0.15 * saddle_term + 0.08 * cross_coupling + 0.05 * additional_coupling
        
        return result