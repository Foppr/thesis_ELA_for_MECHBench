import numpy as np

class ExponentialQuantumSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
        # Exponential decay potential centers and strengths
        self.potential_centers = np.random.uniform(-4.0, 4.0, size=dim)
        self.potential_strengths = np.random.uniform(1.0, 5.0, size=dim)
        self.decay_rates = np.random.uniform(0.5, 2.0, size=dim)
        
        # Quantum-like probability distribution parameters
        self.prob_amplitudes = np.random.uniform(0.5, 2.0, size=dim)
        self.prob_phases = np.random.uniform(0.0, 2*np.pi, size=dim)
        self.prob_frequencies = np.random.uniform(1.0, 4.0, size=dim)
        
        # Dynamic saddle-point field parameters
        self.saddle_centers = np.random.uniform(-3.0, 3.0, size=dim)
        self.saddle_strengths = np.random.uniform(0.5, 3.0, size=dim)
        self.saddle_curvatures = np.random.uniform(0.1, 1.0, size=dim)
        
        # Fractal dimension coupling coefficients
        self.fractal_weights = np.random.uniform(0.1, 1.5, size=(dim, dim))
        self.fractal_exponents = np.random.uniform(0.3, 0.8, size=dim)
        
        # Time-varying harmonic components
        self.time_harmonic_freqs = np.random.uniform(0.5, 3.0, size=dim)
        self.time_harmonic_amps = np.random.uniform(0.1, 1.0, size=dim)
        
        # Cross-dimensional interaction potentials
        self.interaction_strengths = np.random.uniform(0.2, 1.5, size=(dim, dim))
        
        # Stochastic noise fields with varying intensities
        self.noise_intensities = np.random.uniform(0.01, 0.3, size=dim)
        self.noise_frequencies = np.random.uniform(2.0, 8.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potential component
        exp_potential = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.potential_centers[i])
            exp_val = self.potential_strengths[i] * np.exp(-self.decay_rates[i] * dist)
            exp_potential += exp_val
            
        # Quantum-like probability distribution component
        quantum_prob = 0.0
        for i in range(self.dim):
            prob_val = self.prob_amplitudes[i] * np.sin(self.prob_frequencies[i] * x[i] + self.prob_phases[i])**2
            quantum_prob += prob_val
            
        # Dynamic saddle-point field component
        saddle_field = 0.0
        for i in range(self.dim):
            dist = (x[i] - self.saddle_centers[i])**2
            saddle_val = self.saddle_strengths[i] * np.tanh(self.saddle_curvatures[i] * dist)
            saddle_field += saddle_val
            
        # Fractal-based dimension coupling
        fractal_coupling = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.fractal_weights[i, j] * (x[j]**self.fractal_exponents[i])
            fractal_coupling += coupling_sum
            
        # Time-varying harmonic component
        time_harmonic = 0.0
        for i in range(self.dim):
            time_val = self.time_harmonic_amps[i] * np.cos(self.time_harmonic_freqs[i] * x[i])
            time_harmonic += time_val
            
        # Cross-dimensional interaction potentials
        interaction_potential = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(x[i] - x[j])
                    interaction_val = self.interaction_strengths[i, j] * np.exp(-dist)
                    interaction_potential += interaction_val
                    
        # Stochastic noise field
        noise_field = 0.0
        for i in range(self.dim):
            noise_val = self.noise_intensities[i] * np.sin(self.noise_frequencies[i] * x[i])
            noise_field += noise_val
            
        # Combine all components with appropriate weights
        return (1.2 * exp_potential + 
                1.0 * quantum_prob + 
                0.9 * saddle_field + 
                0.8 * fractal_coupling + 
                0.7 * time_harmonic + 
                0.6 * interaction_potential + 
                0.5 * noise_field)