import numpy as np

class HyperChaoticQuantumRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
        # Quantum interference parameters with hyper-chaotic phase modulation
        self.quantum_phases = np.random.uniform(0, 2*np.pi, size=dim)
        self.quantum_amplitudes = np.random.uniform(0.5, 2.0, size=dim)
        self.hyperchaos_params = np.random.uniform(1.0, 3.0, size=dim)
        
        # Radial basis function centers and widths with fractal-like distribution
        self.rbf_centers = np.random.uniform(-4.0, 4.0, size=dim)
        self.rbf_widths = np.random.uniform(0.5, 2.5, size=dim)
        self.rbf_weights = np.random.uniform(0.5, 3.0, size=dim)
        
        # Exponential decay terms with hyper-chaotic time-varying rates
        self.decay_rates = np.random.uniform(0.1, 1.5, size=dim)
        self.decay_amplitudes = np.random.uniform(0.1, 1.0, size=dim)
        self.hyperchaos_decay = np.random.uniform(0.5, 2.0, size=dim)
        
        # Hyper-chaotic cross-dimensional coupling with fractal basin interactions
        self.coupling_matrix = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        self.fractal_coupling = np.random.uniform(0.1, 0.5, size=(dim, dim))
        
        # Frequency modulation with chaotic harmonic components
        self.freq_modulation = np.random.uniform(0.5, 3.0, size=dim)
        self.harmonic_coeffs = np.random.uniform(0.1, 0.8, size=dim)
        
        # Adaptive basin parameters with hyper-chaotic influence and memory effects
        self.basin_centers = np.random.uniform(-3.0, 3.0, size=dim)
        self.basin_strengths = np.random.uniform(1.0, 4.0, size=dim)
        self.basin_radii = np.random.uniform(0.5, 2.0, size=dim)
        self.memory_factors = np.random.uniform(0.5, 1.5, size=dim)
        
        # Additional hyper-chaotic parameters for enhanced complexity
        self.tent_map_params = np.random.uniform(0.8, 1.2, size=dim)
        self.fractal_dimensions = np.random.uniform(1.1, 1.9, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum interference component with hyper-chaotic phase modulation
        quantum_component = 0.0
        for i in range(self.dim):
            # Hyper-chaotic phase modulation using tent map
            chaotic_phase = self.tent_map_params[i] * x[i] * (1 - np.abs(x[i]) / 5.0)
            quantum_val = self.quantum_amplitudes[i] * np.sin(self.quantum_phases[i] + chaotic_phase)
            quantum_component += quantum_val
            
        # Radial basis function component with adaptive centers and fractal influence
        rbf_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.rbf_centers[i])
            # Fractal-like width adjustment
            fractal_width = self.rbf_widths[i] * (1 + 0.2 * np.sin(dist))
            rbf_val = self.rbf_weights[i] * np.exp(-dist**2 / (2 * fractal_width**2))
            rbf_component += rbf_val
            
        # Exponential decay component with hyper-chaotic time-varying rates
        decay_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.basin_centers[i])
            # Hyper-chaotic decay rate modulation
            mod_decay_rate = self.decay_rates[i] * (1 + 0.3 * np.sin(dist))
            decay_val = self.decay_amplitudes[i] * np.exp(-mod_decay_rate * dist)
            decay_component += decay_val
            
        # Dynamic coupling component with fractal basin interactions
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Fractal coupling influence
                    fractal_coupling = self.fractal_coupling[i, j] * (1 + 0.1 * np.cos(x[i] + x[j]))
                    coupling_component += fractal_coupling * self.coupling_matrix[i, j] * x[i] * x[j]
                    
        # Frequency modulation with harmonic components
        freq_component = 0.0
        for i in range(self.dim):
            # Harmonic frequency modulation
            freq_val = np.sin(self.freq_modulation[i] * x[i])
            # Add chaotic harmonic term
            harmonic_term = self.harmonic_coeffs[i] * np.sin(2 * self.freq_modulation[i] * x[i])
            freq_component += freq_val + harmonic_term
            
        # Basin interaction with memory and fractal influence
        basin_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.basin_centers[i])
            # Memory effect on basin strength
            memory_factor = self.memory_factors[i] * (1 + 0.2 * np.sin(dist))
            basin_val = self.basin_strengths[i] * memory_factor * np.exp(-dist / self.basin_radii[i])
            basin_component += basin_val
            
        # Add hyper-chaotic fractal dimension influence
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_component += (self.fractal_dimensions[i] * np.log(1 + np.abs(x[i])))
            
        # Combine all components with different weights and hyper-chaotic scaling
        return (1.5 * quantum_component + 
                2.0 * rbf_component + 
                1.8 * decay_component + 
                1.2 * coupling_component + 
                0.8 * freq_component + 
                1.6 * basin_component + 
                0.5 * fractal_component)