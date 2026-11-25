import numpy as np

class ChaoticNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic neural dynamics parameters
        self.chaotic_params = np.random.uniform(0.1, 2.0, dim)
        self.neural_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.activation_exponents = np.random.uniform(1.5, 4.0, dim)
        # Quantum fractal potential parameters
        self.fractal_dimensions = np.random.uniform(1.2, 2.8, dim)
        self.quantum_coupling = np.random.uniform(0.5, 3.0, dim)
        # Stochastic coupling parameters
        self.stochastic_amplitudes = np.random.uniform(0.1, 1.5, dim)
        self.stochastic_frequencies = np.random.uniform(0.5, 5.0, dim)
        # High-order harmonic interference parameters
        self.harmonic_orders = np.random.randint(3, 12, dim)
        self.interference_strengths = np.random.uniform(0.5, 2.5, dim)
        # Spectral density modulation parameters
        self.spectral_modulation = np.random.uniform(0.1, 1.0, dim)
        self.modulation_frequency = np.random.uniform(1.0, 8.0, dim)
        # Fractal coupling terms
        self.fractal_coupling = np.random.uniform(0.2, 1.8, dim)
        self.coupling_decay = np.random.uniform(0.05, 0.3, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize fitness value
        fitness = 0.0
        
        # Chaotic neural dynamics component
        chaotic_terms = 0.0
        for i in range(self.dim):
            # Apply chaotic neural dynamics with varying activation exponents
            neural_output = 0.0
            for j in range(self.dim):
                weight = self.neural_weights[i, j]
                activation = np.power(np.abs(x[j]), self.activation_exponents[i])
                neural_output += weight * activation
            chaotic_terms += np.sin(neural_output + self.chaotic_params[i])
            
        # Quantum fractal potential component
        quantum_terms = 0.0
        for i in range(self.dim):
            # Apply quantum-like fractal potential with dynamic scaling
            fractal_scale = np.power(1.0 + np.abs(x[i]), self.fractal_dimensions[i])
            quantum_term = np.sin(self.quantum_coupling[i] * x[i]) / fractal_scale
            quantum_terms += quantum_term
            
        # Stochastic coupling component
        stochastic_terms = 0.0
        for i in range(self.dim):
            # Apply stochastic coupling with varying amplitudes and frequencies
            stochastic = self.stochastic_amplitudes[i] * np.sin(
                self.stochastic_frequencies[i] * x[i] + 
                np.random.uniform(0, 2*np.pi)
            )
            stochastic_terms += stochastic
            
        # High-order harmonic interference component
        interference_terms = 0.0
        for i in range(self.dim):
            # Apply high-order harmonic interference with varying strengths
            interference = 0.0
            for k in range(1, self.harmonic_orders[i] + 1):
                freq = k * self.interference_strengths[i]
                amp = 1.0 / (k ** 2.0)
                interference += amp * np.sin(freq * x[i])
            interference_terms += interference
            
        # Spectral density modulation component
        spectral_terms = 0.0
        for i in range(self.dim):
            # Apply spectral density modulation with varying frequencies
            modulation = np.sin(self.modulation_frequency[i] * x[i]) * self.spectral_modulation[i]
            spectral_terms += modulation
            
        # Fractal coupling terms
        fractal_coupling_terms = 0.0
        for i in range(self.dim):
            # Apply fractal coupling with exponential decay
            coupling = self.fractal_coupling[i] * np.exp(-self.coupling_decay[i] * np.abs(x[i]))
            fractal_coupling_terms += coupling * np.sin(x[i])
            
        # Combine all components with weighted contributions
        fitness = 0.25 * chaotic_terms + 0.20 * quantum_terms + 0.15 * stochastic_terms + \
                  0.20 * interference_terms + 0.10 * spectral_terms + 0.10 * fractal_coupling_terms
        
        # Add additional complexity with multi-scale fractal terms
        fractal_complexity = 0.0
        for i in range(self.dim):
            fractal_term = 0.0
            for k in range(1, 25):
                scale = 1.0 / (k ** self.fractal_dimensions[i])
                fractal_term += scale * np.sin(k * x[i] + np.random.uniform(0, 2*np.pi))
            fractal_complexity += fractal_term
            
        fitness += 0.05 * fractal_complexity
        
        # Add quantum harmonic terms for additional complexity
        quantum_harmonic = 0.0
        for i in range(self.dim):
            harmonic_term = 0.0
            for k in range(1, 10):
                freq = k * np.sqrt(np.abs(x[i]) + 1.0)
                amp = 1.0 / (k ** 1.8)
                harmonic_term += amp * np.cos(freq * x[i])
            quantum_harmonic += harmonic_term
            
        fitness += 0.05 * quantum_harmonic
        
        # Add a new component: Multi-peak Gaussian attraction
        gaussian_attraction = 0.0
        for i in range(self.dim):
            # Create multiple local minima using Gaussian attraction points
            attraction_points = np.random.uniform(-4.0, 4.0, 5)
            gaussian_sum = 0.0
            for point in attraction_points:
                gaussian_sum += np.exp(-0.5 * ((x[i] - point) / 0.5) ** 2)
            gaussian_attraction += gaussian_sum
            
        fitness += 0.1 * gaussian_attraction
        
        # Add a new component: Cross-terms with phase shifts
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Phase-shifted cross terms
                phase_shift = np.random.uniform(0, 2*np.pi)
                cross_terms += np.sin(x[i] * x[j] + phase_shift) / (1.0 + abs(x[i]) + abs(x[j]))
                
        fitness += 0.08 * cross_terms
        
        return fitness