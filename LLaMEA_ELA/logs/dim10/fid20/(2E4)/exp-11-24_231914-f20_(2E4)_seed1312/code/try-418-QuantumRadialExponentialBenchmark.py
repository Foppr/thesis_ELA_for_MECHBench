import numpy as np

class QuantumRadialExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
        # Quantum interference parameters with enhanced phase variations
        self.quantum_phases = np.random.uniform(0, 4*np.pi, size=dim)
        self.quantum_amplitudes = np.random.uniform(0.3, 2.5, size=dim)
        
        # Radial basis function centers and widths with adaptive scaling
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=dim)
        self.rbf_widths = np.random.uniform(0.3, 3.0, size=dim)
        self.rbf_weights = np.random.uniform(0.2, 3.5, size=dim)
        
        # Exponential decay parameters with modified rates and amplitudes
        self.decay_rates = np.random.uniform(0.05, 2.0, size=dim)
        self.decay_amplitudes = np.random.uniform(0.05, 1.5, size=dim)
        
        # Enhanced coupling matrix with stronger cross-dimensional interactions
        self.coupling_matrix = np.random.uniform(-1.5, 1.5, size=(dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        
        # Frequency modulation with higher variability
        self.freq_modulation = np.random.uniform(0.3, 4.0, size=dim)
        
        # Enhanced basin parameters with modified radii and strengths
        self.basin_centers = np.random.uniform(-3.5, 3.5, size=dim)
        self.basin_strengths = np.random.uniform(0.8, 5.0, size=dim)
        self.basin_radii = np.random.uniform(0.3, 2.5, size=dim)
        
        # Additional nonlinear coupling terms
        self.nonlinear_coupling = np.random.uniform(-0.5, 0.5, size=(dim, dim))
        np.fill_diagonal(self.nonlinear_coupling, 0.0)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum interference component with enhanced nonlinearity
        quantum_component = 0.0
        for i in range(self.dim):
            quantum_val = self.quantum_amplitudes[i] * np.sin(self.quantum_phases[i] + x[i]**2)
            quantum_component += quantum_val
            
        # Radial basis function component with modified exponential terms
        rbf_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.rbf_centers[i])
            rbf_val = self.rbf_weights[i] * np.exp(-dist**2 / (2 * self.rbf_widths[i]**2)) * np.cos(dist)
            rbf_component += rbf_val
            
        # Exponential decay component with modified decay rates
        decay_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.basin_centers[i])
            decay_val = self.decay_amplitudes[i] * np.exp(-self.decay_rates[i] * dist**1.5)
            decay_component += decay_val
            
        # Enhanced coupling component with nonlinear interactions
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_matrix[i, j] * x[i] * x[j] + self.nonlinear_coupling[i, j] * x[i]**2 * x[j]**2
                    
        # Frequency modulation with higher harmonics
        freq_component = 0.0
        for i in range(self.dim):
            freq_val = np.sin(self.freq_modulation[i] * x[i]) + 0.5 * np.sin(2 * self.freq_modulation[i] * x[i])
            freq_component += freq_val
            
        # Basin interaction with enhanced exponential influence
        basin_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.basin_centers[i])
            basin_val = self.basin_strengths[i] * np.exp(-dist**1.8 / self.basin_radii[i]**1.5)
            basin_component += basin_val
            
        # Combine all components with modified weights
        return (1.8 * quantum_component + 
                2.3 * rbf_component + 
                2.1 * decay_component + 
                1.5 * coupling_component + 
                1.1 * freq_component + 
                1.9 * basin_component)