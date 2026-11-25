import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic logistic map parameters
        self.logistic_r_values = np.random.uniform(3.5, 4.0, dim)
        self.logistic_initials = np.random.uniform(0.1, 0.9, dim)
        # Spectral decomposition components
        self.spectral_frequencies = np.random.uniform(0.5, 5.0, dim)
        self.spectral_amplitudes = np.random.uniform(0.5, 2.0, dim)
        # Quantum tunneling effects
        self.tunneling_probabilities = np.random.uniform(0.01, 0.1, dim)
        self.tunneling_strengths = np.random.uniform(0.1, 1.0, dim)
        # Basin merging parameters
        self.merging_centers = np.random.uniform(-5.0, 5.0, dim)
        self.merging_widths = np.random.uniform(0.5, 2.0, dim)
        self.merging_strengths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic logistic map components
        logistic_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Simulate logistic map dynamics
            xi = self.logistic_initials[i]
            for _ in range(10):  # Let transient die out
                xi = self.logistic_r_values[i] * xi * (1 - xi)
            logistic_values[i] = xi
        
        # Spectral decomposition terms
        spectral_terms = np.zeros(self.dim)
        for i in range(self.dim):
            spectral_terms[i] = self.spectral_amplitudes[i] * np.sin(self.spectral_frequencies[i] * x[i])
        
        # Quantum tunneling effects
        quantum_effects = np.zeros(self.dim)
        for i in range(self.dim):
            # Tunneling probability effect
            tunnel_prob = self.tunneling_probabilities[i]
            tunnel_strength = self.tunneling_strengths[i]
            # Simulate tunneling as a probabilistic shift
            if np.random.random() < tunnel_prob:
                quantum_effects[i] = tunnel_strength * np.sin(x[i] / 2.0)
            else:
                quantum_effects[i] = 0.0
        
        # Basin merging terms
        basin_merges = np.zeros(self.dim)
        for i in range(self.dim):
            center = self.merging_centers[i]
            width = self.merging_widths[i]
            strength = self.merging_strengths[i]
            # Merging effect with Gaussian influence
            basin_merges[i] = strength * np.exp(-((x[i] - center)**2) / (2 * width**2))
        
        # Combine all components
        fitness = 0.0
        for i in range(self.dim):
            # Nonlinear interaction terms
            interaction = 0.0
            for j in range(self.dim):
                if i != j:
                    interaction += np.cos(x[i] - x[j]) * (1 + 0.2 * np.sin(x[i] + x[j]))
            
            # Logistic energy term with improved scaling
            logistic_energy = logistic_values[i]**3 + 0.3 * logistic_values[i]**5
            
            # Spectral contribution with enhanced nonlinearity
            spectral_contribution = spectral_terms[i]**3
            
            # Quantum tunneling effect with modified influence
            quantum_contribution = quantum_effects[i]**3 + 0.1 * quantum_effects[i]**2
            
            # Basin merging component with modified shape
            basin_contribution = basin_merges[i] * (1 + 0.5 * np.sin(x[i]))
            
            # Combine all terms with cross-dimensional coupling
            fitness += logistic_energy + spectral_contribution + quantum_contribution + basin_contribution + interaction
        
        # Normalize and return with improved scaling
        fitness = fitness / (self.dim * 2.0)
        return fitness