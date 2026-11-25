import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize exponential decay parameters
        self.decay_rates = np.random.uniform(0.1, 2.0, size=dim)
        # Initialize sinusoidal frequencies and amplitudes
        self.frequencies = np.random.uniform(1.0, 10.0, size=dim)
        self.amplitudes = np.random.uniform(0.5, 3.0, size=dim)
        # Initialize cubic coupling weights between dimensions
        self.cubic_weights = np.random.uniform(-0.5, 0.5, size=(dim, dim))
        # Dynamic scaling factors for each dimension
        self.scaling_factors = np.random.uniform(0.5, 2.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with sinusoidal modulation
        exp_decay = 0.0
        for i in range(self.dim):
            exp_decay += np.exp(-self.decay_rates[i] * np.abs(x[i])) * \
                        np.sin(self.frequencies[i] * x[i]) * self.amplitudes[i]
            
        # Sinusoidal oscillation component with dynamic scaling
        sin_oscillation = 0.0
        for i in range(self.dim):
            sin_oscillation += (np.sin(self.frequencies[i] * x[i])**3 + 
                              np.cos(self.frequencies[i] * x[i])**2) * \
                             self.scaling_factors[i]
            
        # Adaptive cubic coupling between dimensions
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cubic_coupling += self.cubic_weights[i, j] * (x[i]**3) * (x[j]**3)
            
        # Dynamic phase-shifted harmonic component
        harmonic_phase = 0.0
        for i in range(self.dim):
            phase_shift = np.sin(0.5 * x[i]) * np.cos(0.3 * x[(i+1)%self.dim])
            harmonic_phase += (np.sin(self.frequencies[i] * x[i] + phase_shift) + 
                             0.5 * np.cos(2 * self.frequencies[i] * x[i] + phase_shift)) * \
                            self.amplitudes[i]
            
        # Multi-scale exponential ruggedness with adaptive weights
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += (np.exp(-0.5 * (x[i] - np.mean(x))**2) * 
                          np.sin(15 * x[i]) * np.cos(8 * x[i]) + 
                          0.3 * np.exp(-0.3 * x[i]**2) * np.sin(25 * x[i]))
            
        # Combine all components with optimized weights
        return (1.3 * exp_decay + 
                1.1 * sin_oscillation + 
                1.4 * cubic_coupling + 
                1.2 * harmonic_phase + 
                0.8 * ruggedness)