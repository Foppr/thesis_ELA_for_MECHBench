import numpy as np

class ChaoticRadialQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
        # Chaotic tent map parameters for dynamic landscape generation
        self.chaos_params = np.random.uniform(1.5, 3.0, size=dim)
        
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, size=(dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, size=dim)
        
        # Quantum interference parameters
        self.quantum_phases = np.random.uniform(0, 2*np.pi, size=dim)
        self.quantum_amplitudes = np.random.uniform(0.5, 2.0, size=dim)
        
        # Periodic modulation components
        self.mod_freqs = np.random.uniform(0.1, 1.0, size=dim)
        self.mod_amps = np.random.uniform(0.1, 1.5, size=dim)
        
        # Cross-dimensional coupling with chaotic interaction terms
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, size=(dim, dim))
        
        # Adaptive basin parameters
        self.basin_centers = np.random.uniform(-3.0, 3.0, size=dim)
        self.basin_strengths = np.random.uniform(1.0, 4.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic dynamical component using tent map
        chaotic_component = 0.0
        for i in range(self.dim):
            # Tent map iteration with parameter control
            xi = x[i]
            for _ in range(5):  # Multiple iterations for chaos
                if xi < 0.5:
                    xi = self.chaos_params[i] * xi
                else:
                    xi = self.chaos_params[i] * (1 - xi)
            chaotic_component += xi ** 2
            
        # Radial basis function component
        rbf_component = 0.0
        for i in range(self.dim):
            dist = np.sum((x - self.rbf_centers[:, i]) ** 2)
            rbf_val = np.exp(-dist / (2 * self.rbf_widths[i] ** 2))
            rbf_component += rbf_val
            
        # Quantum interference pattern
        quantum_component = 0.0
        for i in range(self.dim):
            phase = self.quantum_phases[i] + x[i]
            amplitude = self.quantum_amplitudes[i]
            quantum_component += amplitude * np.sin(phase) * np.cos(phase)
            
        # Periodic modulation component
        mod_component = 0.0
        for i in range(self.dim):
            mod_val = self.mod_amps[i] * np.sin(self.mod_freqs[i] * x[i])
            mod_component += mod_val
            
        # Cross-dimensional coupling with chaotic interaction
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_matrix[i, j] * x[i] * x[j]
                    
        # Basin attraction component
        basin_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.basin_centers[i])
            basin_val = self.basin_strengths[i] * (dist ** 2) / (1 + dist)
            basin_component += basin_val
            
        # Combine all components with adaptive weights
        return (0.8 * chaotic_component + 
                1.2 * rbf_component + 
                0.9 * quantum_component + 
                0.7 * mod_component + 
                0.6 * coupling_component + 
                1.0 * basin_component)