import numpy as np

class QuantumFractalOscillator:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal harmonic parameters
        self.oscillator_freq = np.random.uniform(1.0, 10.0, dim)
        self.oscillator_amp = np.random.uniform(0.5, 3.0, dim)
        self.fractal_dim = np.random.uniform(1.1, 2.8, dim)
        self.phase_coupling = np.random.uniform(0.5, 3.0, (dim, dim))  # Increased coupling range
        self.quantum_coeff = np.random.uniform(0.5, 3.0, dim)
        self.basin_centers = np.random.uniform(-4.0, 4.0, (dim, 8))
        self.basin_widths = np.random.uniform(0.5, 2.5, (dim, 8))
        self.harmonic_order = np.random.randint(3, 15, dim)
        self.fractal_scale = np.random.uniform(0.1, 1.0, dim)
        self.oscillator_damping = np.random.uniform(0.05, 0.3, dim)  # Increased damping
        self.quantum_phase_shift = np.random.uniform(0, 2*np.pi, dim)
        self.nested_freq = np.random.uniform(0.5, 5.0, dim)
        self.adaptive_weight = np.random.uniform(0.5, 2.0, dim)
        # Add chaotic damping parameter
        self.chaotic_damping = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize fitness value
        fitness = 0.0
        
        # Add nested harmonic oscillator terms
        for i in range(self.dim):
            oscillator_term = 0.0
            # Base harmonic oscillator with fractal scaling
            base_freq = self.oscillator_freq[i] * (1.0 + 0.3 * np.sin(x[i]))
            oscillator_term += self.oscillator_amp[i] * np.sin(base_freq * x[i])
            
            # Add higher order harmonics with adaptive weights
            for k in range(2, self.harmonic_order[i] + 1):
                harmonic_freq = base_freq * k
                harmonic_amp = self.oscillator_amp[i] / (k**self.fractal_dim[i])
                oscillator_term += harmonic_amp * np.sin(harmonic_freq * x[i])
            
            # Add nested oscillation with different frequency
            nested_freq = self.nested_freq[i] * (1.0 + 0.2 * np.cos(x[i]))
            oscillator_term += 0.5 * np.sin(nested_freq * x[i])
            
            # Apply quantum phase modulation
            quantum_phase = self.quantum_coeff[i] * np.sin(x[i] + self.quantum_phase_shift[i])
            oscillator_term *= (1.0 + 0.3 * np.sin(quantum_phase))
            
            # Add chaotic damping effect
            chaotic_factor = 1.0 + self.chaotic_damping[i] * np.sin(5.0 * x[i])
            oscillator_term *= chaotic_factor
            
            fitness += oscillator_term
            
        # Add fractal basin attraction terms
        basin_terms = 0.0
        for i in range(self.dim):
            basin_attraction = 0.0
            for j in range(8):  # 8 basin centers per dimension
                center = self.basin_centers[i, j]
                width = self.basin_widths[i, j]
                # Fractal basin potential with quantum interference
                distance = np.abs(x[i] - center)
                basin_potential = np.exp(-0.5 * (distance / width)**2)
                
                # Add quantum harmonic interference
                quantum_interference = np.sin(self.quantum_coeff[i] * distance) * \
                                     np.cos(self.quantum_coeff[i] * distance)
                basin_attraction += basin_potential * (1.0 + 0.2 * quantum_interference)
            basin_terms += basin_attraction
            
        # Add phase-coupling between dimensions
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.phase_coupling[i, j] * np.sin(x[i] + x[j])
                coupling_terms += coupling
                
        # Add adaptive fractal scaling terms
        fractal_terms = 0.0
        for i in range(self.dim):
            fractal_term = 0.0
            # Multi-scale fractal contribution
            for k in range(1, 8):
                scale = self.fractal_scale[i] * (k**self.fractal_dim[i])
                fractal_term += np.sin(scale * x[i]) * np.cos(scale * x[i])
            fractal_terms += fractal_term
            
        # Add quantum harmonic resonance terms
        quantum_harmonic_terms = 0.0
        for i in range(self.dim):
            harmonic_sum = 0.0
            for k in range(1, 6):
                freq = self.oscillator_freq[i] * k
                amp = self.adaptive_weight[i] / (k**1.5)
                harmonic_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            quantum_harmonic_terms += harmonic_sum
            
        # Combine all components with appropriate weights
        total = 0.3 * fitness + 0.25 * basin_terms + 0.2 * coupling_terms + 0.15 * fractal_terms + 0.1 * quantum_harmonic_terms
        
        return total