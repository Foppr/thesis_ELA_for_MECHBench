import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize exponential decay parameters with chaotic variation
        self.decay_rates = np.random.uniform(0.05, 3.0, size=dim)
        # Initialize sinusoidal frequencies and amplitudes with quantum-like spacing
        self.frequencies = np.random.uniform(1.0, 15.0, size=dim)
        self.amplitudes = np.random.uniform(0.2, 4.0, size=dim)
        # Initialize cubic coupling weights with fractal scaling
        self.cubic_weights = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Dynamic scaling factors with chaotic behavior
        self.scaling_factors = np.random.uniform(0.3, 2.5, size=dim)
        # Quantum interference parameters with phase modulation
        self.interference_freq = np.random.uniform(0.1, 8.0, size=dim)
        self.interference_amp = np.random.uniform(0.05, 1.5, size=dim)
        # Fractal ruggedness enhancement parameters
        self.ruggedness_strength = np.random.uniform(1.0, 3.0, size=dim)
        self.ruggedness_frequency = np.random.uniform(2.0, 20.0, size=dim)
        # Chaotic additional components
        self.chaotic_coeffs = np.random.uniform(-0.5, 0.5, size=dim)
        # Additional chaotic parameters for enhanced complexity
        self.chaotic_phase_shifts = np.random.uniform(0.1, 2.0, size=dim)
        self.fractal_exponents = np.random.uniform(0.5, 2.5, size=dim)
        self.quantum_coupling = np.random.uniform(-0.3, 0.3, size=(dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay with chaotic sinusoidal modulation
        exp_decay = 0.0
        for i in range(self.dim):
            exp_decay += np.exp(-self.decay_rates[i] * np.abs(x[i])) * \
                        np.sin(self.frequencies[i] * x[i]) * self.amplitudes[i]
            
        # Sinusoidal oscillation with quantum-like phase interference
        sin_oscillation = 0.0
        for i in range(self.dim):
            sin_oscillation += (np.sin(self.frequencies[i] * x[i])**3 + 
                              np.cos(self.frequencies[i] * x[i])**2) * \
                             self.scaling_factors[i]
            
        # Adaptive cubic coupling with fractal dimensionality
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cubic_coupling += self.cubic_weights[i, j] * (x[i]**3) * (x[j]**3)
            
        # Quantum-like harmonic phase with chaotic interference
        harmonic_phase = 0.0
        for i in range(self.dim):
            phase_shift = np.sin(0.7 * x[i]) * np.cos(0.4 * x[(i+1)%self.dim])
            harmonic_phase += (np.sin(self.frequencies[i] * x[i] + phase_shift) + 
                             0.3 * np.cos(2 * self.frequencies[i] * x[i] + phase_shift)) * \
                            self.amplitudes[i]
            
        # Fractal ruggedness with chaotic enhancement
        ruggedness = 0.0
        for i in range(self.dim):
            # Base fractal ruggedness component
            base_rugged = (np.exp(-0.3 * (x[i] - np.mean(x))**2) * 
                          np.sin(self.ruggedness_frequency[i] * x[i]) * 
                          np.cos(self.ruggedness_frequency[i] * x[i] / 3))
            # Interference term with chaotic amplitude
            interference = self.interference_amp[i] * np.sin(self.interference_freq[i] * x[i])
            # Fractal quadratic ruggedness component
            fractal_rugged = self.ruggedness_strength[i] * (x[i]**2 - 4*x[i] + 4) * \
                           np.sin(10 * x[i])
            ruggedness += base_rugged + 0.5 * interference + 0.2 * fractal_rugged
            
        # Chaotic multiscale exponential component with quantum-like behavior
        multiscale = 0.0
        for i in range(self.dim):
            multiscale += (np.exp(-0.4 * x[i]**2) * np.sin(30 * x[i]) + 
                          0.6 * np.exp(-0.15 * (x[i] - 2)**2) * np.cos(15 * x[i]) +
                          0.4 * np.exp(-0.25 * (x[i] + 3)**2) * np.sin(20 * x[i]) +
                          self.chaotic_coeffs[i] * np.sin(50 * x[i]))
            
        # Quantum coupling enhancement with fractal scaling
        quantum_enhancement = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    quantum_enhancement += self.quantum_coupling[i, j] * np.sin(x[i]) * np.cos(x[j])
        
        # Fractal dimensionality scaling
        fractal_scaling = 0.0
        for i in range(self.dim):
            fractal_scaling += (np.abs(x[i])**self.fractal_exponents[i]) * np.sin(self.frequencies[i] * x[i])
            
        # Combine all components with enhanced weights for chaotic behavior
        return (1.2 * exp_decay + 
                1.5 * sin_oscillation + 
                1.6 * cubic_coupling + 
                1.3 * harmonic_phase + 
                0.9 * ruggedness + 
                0.7 * multiscale +
                0.5 * quantum_enhancement +
                0.4 * fractal_scaling)