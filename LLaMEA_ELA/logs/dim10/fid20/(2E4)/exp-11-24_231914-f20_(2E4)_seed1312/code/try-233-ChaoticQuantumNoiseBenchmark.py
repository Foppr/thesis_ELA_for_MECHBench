import numpy as np

class ChaoticQuantumNoiseBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave parameters
        self.chaos_freq = np.random.uniform(2.0, 15.0, size=dim)
        self.chaos_amp = np.random.uniform(1.0, 4.0, size=dim)
        self.chaos_phase = np.random.uniform(0, 4*np.pi, size=dim)
        # Quantum-like probability distribution parameters
        self.quantum_centers = np.random.uniform(-4.0, 4.0, size=(dim, 8))
        self.quantum_widths = np.random.uniform(0.3, 2.5, size=8)
        self.quantum_weights = np.random.uniform(-3.0, 3.0, size=8)
        # Dynamic terrain scaling parameters
        self.scaling_factors = np.random.uniform(0.5, 2.0, size=dim)
        self.scaling_frequency = np.random.uniform(1.0, 5.0, size=dim)
        # Multi-scale interaction terms with quantum coupling
        self.quantum_coupling = np.random.uniform(-1.5, 1.5, size=(dim, dim))
        # Basin-like regions with quantum wells
        self.well_centers = np.random.uniform(-4.0, 4.0, size=6)
        self.well_radii = np.random.uniform(0.3, 1.8, size=6)
        self.well_depths = np.random.uniform(2.0, 6.0, size=6)
        # Chaos control parameters
        self.chaos_control = np.random.uniform(0.1, 0.9, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component
        chaos_component = 0.0
        for i in range(self.dim):
            chaos_val = self.chaos_amp[i] * np.sin(self.chaos_freq[i] * x[i] + self.chaos_phase[i])
            # Add chaotic modulation
            chaos_val *= (1.0 + self.chaos_control[i] * np.sin(3.0 * x[i]))
            chaos_component += chaos_val
            
        # Quantum-like probability distribution component
        quantum_component = 0.0
        for j in range(8):
            quantum_val = 0.0
            for i in range(self.dim):
                quantum_val += (x[i] - self.quantum_centers[i, j])**2
            quantum_component += self.quantum_weights[j] * np.exp(-quantum_val / (2 * self.quantum_widths[j]**2))
            
        # Dynamic terrain scaling component
        scaling_component = 0.0
        for i in range(self.dim):
            scaling_val = self.scaling_factors[i] * np.cos(self.scaling_frequency[i] * x[i])
            scaling_component += scaling_val
            
        # Multi-scale interaction terms with quantum coupling
        interaction_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_component += self.quantum_coupling[i, j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Quantum well basin component
        well_component = 0.0
        for i in range(self.dim):
            min_dist = float('inf')
            for k in range(6):
                dist = np.abs(x[i] - self.well_centers[k])
                if dist < min_dist:
                    min_dist = dist
            if min_dist <= self.well_radii[k]:
                well_component += self.well_depths[k] * (1 - min_dist / self.well_radii[k])**2
            
        # Combined fitness function with balanced weights
        return (1.5 * chaos_component + 
                1.8 * quantum_component + 
                1.0 * scaling_component + 
                1.4 * interaction_component + 
                0.9 * well_component)