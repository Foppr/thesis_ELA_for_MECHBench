import numpy as np

class QuantumHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum oscillator parameters
        self.frequencies = np.random.uniform(0.5, 3.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Coupling parameters between dimensions
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0)
        # Phase interference parameters
        self.interference_strengths = np.random.uniform(0.1, 1.5, dim)
        self.wave_lengths = np.random.uniform(1.0, 4.0, dim)
        # Quantum potential parameters
        self.quantum_potential_strength = np.random.uniform(0.5, 2.0, dim)
        self.potential_offsets = np.random.uniform(-1.0, 1.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Quantum harmonic oscillator component for each dimension
        for i in range(self.dim):
            # Quantum harmonic oscillator potential
            oscillator_term = self.amplitudes[i] * (x[i] - self.phases[i])**2
            
            # Add quantum potential term
            quantum_potential = self.quantum_potential_strength[i] * np.exp(-0.5 * (x[i] - self.potential_offsets[i])**2)
            
            # Wave interference component
            wave_component = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_matrix[i][j]
                    wave_component += coupling * np.sin(self.wave_lengths[j] * x[j])
            
            # Combine components with interference
            interference = self.interference_strengths[i] * np.sin(self.frequencies[i] * x[i] + wave_component)
            
            result += oscillator_term + quantum_potential + interference**2
            
        # Cross-dimensional quantum coupling terms
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += self.coupling_matrix[i][j] * np.cos(self.frequencies[i] * x[i]) * np.sin(self.frequencies[j] * x[j])
        
        result += 0.5 * coupling_terms**2
        
        # Add periodic modulation based on all dimensions
        periodic_modulation = 0.0
        for i in range(self.dim):
            periodic_modulation += np.cos(self.wave_lengths[i] * x[i]) * np.sin(self.frequencies[i] * x[i])
            
        result += 0.3 * periodic_modulation**2
        
        # Add noise and normalize
        noise = np.random.normal(0, 0.1, self.dim)
        result += 0.1 * np.sum(noise * x)
        
        # Final normalization
        result = result / (self.dim + 1.0) + 0.2 * np.sum(x**4) / self.dim
        
        return result