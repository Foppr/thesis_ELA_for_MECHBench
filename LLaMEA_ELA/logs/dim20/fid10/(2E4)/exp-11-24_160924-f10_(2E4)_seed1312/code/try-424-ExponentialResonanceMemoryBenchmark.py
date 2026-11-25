import numpy as np

class ExponentialResonanceMemoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize exponential decay parameters
        self.decay_rates = np.random.uniform(0.1, 2.0, dim)
        self.decay_amplitudes = np.random.uniform(1.0, 5.0, dim)
        # Trigonometric resonance components
        self.resonance_freqs = np.random.uniform(1.0, 8.0, dim)
        self.resonance_amps = np.random.uniform(0.5, 3.0, dim)
        self.resonance_phases = np.random.uniform(0.0, 2*np.pi, dim)
        # Spherical harmonic interaction parameters
        self.sphere_harmonic_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.sphere_radii = np.random.uniform(0.5, 3.0, dim)
        # Temporal memory effects
        self.memory_dampings = np.random.uniform(0.01, 0.2, dim)
        self.memory_delays = np.random.uniform(0.1, 1.0, dim)
        # Cross-dimensional coupling terms
        self.coupling_strengths = np.random.uniform(0.3, 1.5, (dim, dim))
        # Additional noise and perturbation parameters
        self.noise_level = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Exponential decay components
        for i in range(self.dim):
            result += self.decay_amplitudes[i] * np.exp(-self.decay_rates[i] * np.abs(x[i]))
            
        # Trigonometric resonance terms
        for i in range(self.dim):
            result += self.resonance_amps[i] * np.sin(self.resonance_freqs[i] * x[i] + self.resonance_phases[i])
            result += self.resonance_amps[i] * np.cos(self.resonance_freqs[i] * x[i] + self.resonance_phases[i])
            
        # Spherical harmonic interactions
        for i in range(self.dim):
            sphere_sum = 0.0
            for j in range(self.dim):
                # Spherical distance component
                dist = np.sqrt(np.sum((x - self.sphere_harmonic_coeffs[i]) ** 2))
                sphere_sum += self.sphere_harmonic_coeffs[i][j] * np.sin(dist / self.sphere_radii[i])
            result += sphere_sum
            
        # Cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    result += self.coupling_strengths[i][j] * np.exp(-np.abs(x[i] - x[j])) * np.sin(x[i] * x[j])
                    
        # Temporal memory effects
        for i in range(self.dim):
            # Simple memory term with exponential decay
            memory_effect = self.memory_dampings[i] * np.exp(-self.memory_delays[i] * np.abs(x[i]))
            result += memory_effect
            
        # Higher-order polynomial and interaction terms
        for i in range(self.dim):
            result += 0.5 * x[i]**4 - 1.2 * x[i]**3 + 0.8 * x[i]**2 - 0.3 * x[i]
            
        # Add noise component to increase robustness
        noise = np.sum(np.random.normal(0, self.noise_level))
        result += noise
        
        return result