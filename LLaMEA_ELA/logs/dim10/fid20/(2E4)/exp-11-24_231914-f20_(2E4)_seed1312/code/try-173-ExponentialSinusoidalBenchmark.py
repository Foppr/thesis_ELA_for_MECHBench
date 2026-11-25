import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize exponential decay parameters with chaotic variation
        self.decay_rates = np.random.uniform(0.05, 3.0, size=dim)
        # Initialize sinusoidal frequencies and amplitudes with chaotic scaling
        self.frequencies = np.random.uniform(0.5, 15.0, size=dim)
        self.amplitudes = np.random.uniform(0.2, 4.0, size=dim)
        # Initialize cubic coupling weights with enhanced complexity
        self.cubic_weights = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Dynamic scaling factors for each dimension with chaotic modulation
        self.scaling_factors = np.random.uniform(0.3, 2.5, size=dim)
        # Additional chaotic interference parameters
        self.interference_freq = np.random.uniform(1.0, 8.0, size=dim)
        self.interference_amp = np.random.uniform(0.05, 1.5, size=dim)
        # Ruggedness enhancement with chaotic components
        self.ruggedness_factors = np.random.uniform(0.05, 3.0, size=dim)
        self.modulation_freq = np.random.uniform(1.0, 12.0, size=dim)
        # Chaotic modulation parameters for enhanced landscape complexity
        self.chaos_params = np.random.uniform(0.1, 0.9, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with chaotic modulation
        exp_decay = 0.0
        for i in range(self.dim):
            exp_decay += np.exp(-self.decay_rates[i] * np.abs(x[i])) * \
                        np.sin(self.frequencies[i] * x[i]) * self.amplitudes[i] * \
                        (1.0 + 0.2 * np.sin(self.chaos_params[i] * x[i]))
            
        # Augmented sinusoidal oscillation with chaotic interference
        sin_oscillation = 0.0
        for i in range(self.dim):
            sin_oscillation += (np.sin(self.frequencies[i] * x[i])**4 + 
                              np.cos(self.frequencies[i] * x[i])**3) * \
                             self.scaling_factors[i] * \
                             (1.0 + 0.15 * np.cos(self.chaos_params[i] * x[i]))
            
        # Strengthened adaptive cubic coupling with chaotic interaction
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cubic_coupling += self.cubic_weights[i, j] * (x[i]**3) * (x[j]**3) * \
                                    (1.0 + 0.2 * np.sin(self.chaos_params[i] * x[j]))
            
        # Chaotic harmonic phase component with multi-frequency interference
        harmonic_phase = 0.0
        for i in range(self.dim):
            phase_shift = np.sin(0.7 * x[i]) * np.cos(0.4 * x[(i+1)%self.dim])
            harmonic_phase += (np.sin(self.frequencies[i] * x[i] + phase_shift) + 
                             0.3 * np.cos(2 * self.frequencies[i] * x[i] + phase_shift) + \
                             0.1 * np.sin(3 * self.frequencies[i] * x[i] + phase_shift)) * \
                            self.amplitudes[i] * \
                            (1.0 + 0.1 * np.cos(self.chaos_params[i] * x[i]))
            
        # Enhanced ruggedness with chaotic modulation and interference
        ruggedness = 0.0
        for i in range(self.dim):
            base_rugged = (np.exp(-0.3 * (x[i] - np.mean(x))**2) * 
                          np.sin(20 * x[i]) * np.cos(12 * x[i]))
            interference = self.interference_amp[i] * np.sin(self.interference_freq[i] * x[i])
            modulation = 1.0 + 0.4 * np.sin(self.modulation_freq[i] * x[i]) * \
                        np.cos(self.chaos_params[i] * x[i])
            ruggedness += (base_rugged + 0.5 * interference) * modulation * self.ruggedness_factors[i]
            
        # Multi-scale chaotic exponential component
        multiscale = 0.0
        for i in range(self.dim):
            multiscale += (np.exp(-0.2 * x[i]**2) * np.sin(30 * x[i]) + 
                          0.7 * np.exp(-0.15 * (x[i] - 2)**2) * np.cos(15 * x[i]) + \
                          0.3 * np.exp(-0.1 * (x[i] + 2)**2) * np.sin(8 * x[i])) * \
                         (1.0 + 0.3 * np.sin(self.chaos_params[i] * x[i]))
            
        # Chaotic noise reduction component
        noise_reduction = 0.0
        for i in range(self.dim):
            noise_reduction += 0.1 * np.sin(5 * x[i]) * np.cos(9 * x[i]) * \
                            (1.0 + 0.2 * np.cos(self.chaos_params[i] * x[i]))
            
        # Combine all components with optimized weights for enhanced challenge
        return (1.2 * exp_decay + 
                1.5 * sin_oscillation + 
                1.8 * cubic_coupling + 
                1.3 * harmonic_phase + 
                1.0 * ruggedness + 
                0.9 * multiscale + 
                0.2 * noise_reduction)