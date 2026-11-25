import numpy as np

class QuantumHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters
        self.omega = np.random.uniform(0.5, 2.0, dim)
        self.mass = np.random.uniform(0.8, 1.5, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Adaptive coupling strengths between dimensions
        self.coupling_strengths = np.random.uniform(0.1, 1.0, (dim, dim))
        np.fill_diagonal(self.coupling_strengths, 0)
        # Entropic basin parameters
        self.basin_centers = np.random.uniform(-3.0, 3.0, dim)
        self.basin_widths = np.random.uniform(0.5, 2.0, dim)
        self.basin_depths = np.random.uniform(1.0, 5.0, dim)
        # Dynamic phase transition parameters
        self.transition_points = np.random.uniform(-4.0, 4.0, dim)
        self.transition_widths = np.random.uniform(0.3, 1.0, dim)
        # Quantum tunneling effects
        self.tunneling_probabilities = np.random.uniform(0.05, 0.3, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic potential terms
        quantum_harmonic = np.zeros(self.dim)
        for i in range(self.dim):
            # Quantum harmonic oscillator energy
            harmonic_energy = 0.5 * self.mass[i] * (self.omega[i]**2) * (x[i] - self.basin_centers[i])**2
            quantum_harmonic[i] = harmonic_energy
        
        # Entropic basin attraction terms
        basin_terms = np.zeros(self.dim)
        for i in range(self.dim):
            # Gaussian basin with entropy-based weighting
            basin_attraction = self.basin_depths[i] * np.exp(-((x[i] - self.basin_centers[i])**2) / (2 * self.basin_widths[i]**2))
            # Add entropy factor that changes based on position
            entropy_factor = 1.0 + 0.5 * np.sin(x[i])
            basin_terms[i] = basin_attraction * entropy_factor
        
        # Coupling between dimensions (quantum-like entanglement)
        coupling_terms = np.zeros(self.dim)
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strengths[i, j] * np.sin(x[i] - x[j])
            coupling_terms[i] = coupling_sum
        
        # Dynamic phase transition effects
        phase_transitions = np.zeros(self.dim)
        for i in range(self.dim):
            # Sigmoidal transition function
            transition_effect = 1.0 / (1.0 + np.exp(-((x[i] - self.transition_points[i]) / self.transition_widths[i])))
            phase_transitions[i] = transition_effect * np.sin(x[i])
        
        # Quantum tunneling probability effect
        tunneling_effects = np.zeros(self.dim)
        for i in range(self.dim):
            # Random tunneling effect based on probability
            if np.random.rand() < self.tunneling_probabilities[i]:
                tunneling_effects[i] = np.random.normal(0, 0.5)
        
        # Combine all components
        fitness = 0.0
        for i in range(self.dim):
            # Nonlinear interaction between all components
            total_contribution = (
                quantum_harmonic[i] + 
                basin_terms[i] + 
                coupling_terms[i]**2 + 
                phase_transitions[i]**2 + 
                tunneling_effects[i]
            )
            
            # Add dimension-specific noise
            noise = np.random.normal(0, 0.1)
            fitness += total_contribution + noise
        
        # Normalize by dimension
        fitness = fitness / self.dim
        return fitness