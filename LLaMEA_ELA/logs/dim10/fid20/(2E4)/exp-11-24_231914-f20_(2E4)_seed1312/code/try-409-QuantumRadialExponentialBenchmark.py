import numpy as np

class QuantumRadialExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
        # Quantum interference parameters
        self.quantum_phases = np.random.uniform(0, 2*np.pi, size=dim)
        self.quantum_amplitudes = np.random.uniform(0.5, 2.0, size=dim)
        
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, size=dim)
        self.rbf_widths = np.random.uniform(0.5, 2.5, size=dim)
        self.rbf_weights = np.random.uniform(0.5, 3.0, size=dim)
        
        # Exponential decay parameters with time-varying rates
        self.decay_rates = np.random.uniform(0.1, 1.5, size=dim)
        self.decay_amplitudes = np.random.uniform(0.1, 1.0, size=dim)
        
        # Dynamic coupling coefficients between dimensions
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, size=(dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        
        # Frequency modulation for dynamic landscape
        self.freq_modulation = np.random.uniform(0.5, 3.0, size=dim)
        
        # Adaptive basin parameters with exponential influence
        self.basin_centers = np.random.uniform(-3.0, 3.0, size=dim)
        self.basin_strengths = np.random.uniform(1.0, 4.0, size=dim)
        self.basin_radii = np.random.uniform(0.5, 2.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum interference component
        quantum_component = 0.0
        for i in range(self.dim):
            quantum_val = self.quantum_amplitudes[i] * np.sin(self.quantum_phases[i] + x[i])
            quantum_component += quantum_val
            
        # Radial basis function component with adaptive centers
        rbf_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.rbf_centers[i])
            rbf_val = self.rbf_weights[i] * np.exp(-dist**2 / (2 * self.rbf_widths[i]**2))
            rbf_component += rbf_val
            
        # Exponential decay component
        decay_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.basin_centers[i])
            decay_val = self.decay_amplitudes[i] * np.exp(-self.decay_rates[i] * dist)
            decay_component += decay_val
            
        # Dynamic coupling component
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_matrix[i, j] * x[i] * x[j]
                    
        # Frequency modulation component
        freq_component = 0.0
        for i in range(self.dim):
            freq_val = np.sin(self.freq_modulation[i] * x[i])
            freq_component += freq_val
            
        # Basin interaction with exponential influence
        basin_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.basin_centers[i])
            basin_val = self.basin_strengths[i] * np.exp(-dist / self.basin_radii[i])
            basin_component += basin_val
            
        # Combine all components with different weights
        return (1.2 * quantum_component + 
                1.8 * rbf_component + 
                1.5 * decay_component + 
                0.9 * coupling_component + 
                0.7 * freq_component + 
                1.3 * basin_component)