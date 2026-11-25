import numpy as np

class QuantumFractalOscillator:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters
        self.omega = np.random.uniform(0.5, 3.0, dim)
        self.quantum_number = np.random.randint(1, 10, dim)
        self.phase_shift = np.random.uniform(0, 2*np.pi, dim)
        self.quantum_coeff = np.random.uniform(0.1, 2.0, dim)
        
        # Fractal basin parameters
        self.fractal_dim = np.random.uniform(1.1, 2.9, dim)
        self.basin_scale = np.random.uniform(0.5, 3.0, dim)
        self.attractor_positions = np.random.uniform(-4.0, 4.0, (dim, 8))
        self.basin_strength = np.random.uniform(0.5, 2.0, dim)
        
        # Stochastic resonance parameters
        self.noise_amplitude = np.random.uniform(0.1, 1.0, dim)
        self.resonance_frequency = np.random.uniform(0.1, 2.0, dim)
        self.damping_coeff = np.random.uniform(0.01, 0.5, dim)
        
        # Coupling and interference terms (modified)
        self.coupling_strength = np.random.uniform(0.2, 2.0, (dim, dim))  # Increased range
        self.interference_phase = np.random.uniform(0, 2*np.pi, (dim, dim))
        self.fractal_coupling = np.random.uniform(0.02, 0.5, (dim, dim))  # Increased range
        
        # Multi-scale harmonic parameters
        self.harmonic_orders = np.random.randint(2, 15, dim)
        self.scale_factors = np.random.uniform(0.1, 2.0, dim)
        self.multi_scale_exponent = np.random.uniform(0.5, 2.5, dim)
        
        # Added polynomial chaos terms for increased complexity
        self.poly_chaos_degree = np.random.randint(3, 7, dim)
        self.poly_chaos_coeff = np.random.uniform(-0.5, 0.5, (dim, 4))
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic potential terms
        quantum_terms = 0.0
        for i in range(self.dim):
            omega = self.omega[i]
            n = self.quantum_number[i]
            phase = self.phase_shift[i]
            coeff = self.quantum_coeff[i]
            
            # Quantum harmonic oscillator energy
            energy = (n + 0.5) * omega
            # Add quantum correction term
            quantum_corr = coeff * np.sin(omega * x[i] + phase)
            quantum_terms += energy + quantum_corr
            
        # Fractal basin attraction terms
        basin_terms = 0.0
        for i in range(self.dim):
            min_distance = float('inf')
            for j in range(8):
                dist = abs(x[i] - self.attractor_positions[i, j])
                if dist < min_distance:
                    min_distance = dist
            
            # Fractal basin potential
            fractal_potential = self.basin_strength[i] * (min_distance ** self.fractal_dim[i])
            basin_terms += fractal_potential
            
        # Stochastic resonance terms
        resonance_terms = 0.0
        for i in range(self.dim):
            noise = self.noise_amplitude[i] * np.random.normal(0, 1)
            freq = self.resonance_frequency[i]
            damping = self.damping_coeff[i]
            
            # Resonance term with damping
            resonance = (np.sin(freq * x[i]) + noise) * np.exp(-damping * abs(x[i]))
            resonance_terms += resonance
            
        # Coupling and interference terms
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_strength[i, j] * np.cos(self.interference_phase[i, j])
                    coupling_terms += coupling * np.sin(x[i] - x[j])
                    
        # Multi-scale harmonic terms
        harmonic_terms = 0.0
        for i in range(self.dim):
            scale = self.scale_factors[i]
            exponent = self.multi_scale_exponent[i]
            order = self.harmonic_orders[i]
            
            harmonic_sum = 0.0
            for k in range(1, order + 1):
                freq = k * scale
                harmonic_sum += (1.0/k) * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
            # Multi-scale fractal modification
            multi_scale_factor = scale ** exponent
            harmonic_terms += multi_scale_factor * harmonic_sum
            
        # Added polynomial chaos terms
        poly_chaos_terms = 0.0
        for i in range(self.dim):
            poly_sum = 0.0
            for k in range(1, self.poly_chaos_degree[i] + 1):
                poly_sum += self.poly_chaos_coeff[i, k-1] * (x[i] ** k)
            poly_chaos_terms += poly_sum
            
        # Combine all terms with adaptive weights
        total = 0.25 * quantum_terms + 0.2 * basin_terms + 0.15 * resonance_terms + 0.2 * coupling_terms + 0.15 * harmonic_terms + 0.05 * poly_chaos_terms
        
        return total