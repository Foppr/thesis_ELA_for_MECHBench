import numpy as np

class QuantumResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters with complex phase relationships
        self.oscillator_freq = np.random.uniform(0.5, 3.0, size=dim)
        self.oscillator_amp = np.random.uniform(0.1, 2.0, size=dim)
        self.oscillator_phase = np.random.uniform(0, 2*np.pi, size=dim)
        self.oscillator_damping = np.random.uniform(0.01, 0.5, size=dim)
        
        # Radial basis function network parameters with adaptive centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(20, dim))
        self.rbf_widths = np.random.uniform(0.1, 2.0, size=20)
        self.rbf_weights = np.random.uniform(-1.0, 1.0, size=20)
        
        # Stochastic resonance parameters with multiplicative noise
        self.resonance_strength = np.random.uniform(0.1, 2.0, size=dim)
        self.noise_intensity = np.random.uniform(0.01, 0.5, size=dim)
        self.resonance_freq = np.random.uniform(0.1, 1.0, size=dim)
        
        # Quantum tunneling parameters for basin hopping
        self.tunnel_prob = np.random.uniform(0.001, 0.1, size=dim)
        self.tunnel_distance = np.random.uniform(0.5, 3.0, size=dim)
        
        # Coupling coefficients between dimensions
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, size=(dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0)
        
        # Nonlinear transformation parameters
        self.nonlin_power = np.random.uniform(1.5, 4.0, size=dim)
        self.nonlin_shift = np.random.uniform(-1.0, 1.0, size=dim)
        
        # Multi-scale fractal modulation with quantum-like interference
        self.fractal_scale = np.random.uniform(0.1, 1.0, size=dim)
        self.fractal_freq = np.random.uniform(1.0, 10.0, size=dim)
        self.interference_strength = np.random.uniform(0.1, 1.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator component
        quantum_component = 0.0
        for i in range(self.dim):
            freq = self.oscillator_freq[i]
            amp = self.oscillator_amp[i]
            phase = self.oscillator_phase[i]
            damping = self.oscillator_damping[i]
            
            # Quantum-like oscillation with damping
            oscillator_val = amp * np.sin(freq * x[i] + phase) * np.exp(-damping * x[i]**2)
            quantum_component += oscillator_val
            
        # Radial basis function network component
        rbf_component = 0.0
        for i in range(20):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            weight = self.rbf_weights[i]
            
            # RBF with Gaussian kernel
            dist = np.sum((x - center)**2)
            rbf_val = weight * np.exp(-dist / (2 * width**2))
            rbf_component += rbf_val
            
        # Stochastic resonance component
        resonance_component = 0.0
        for i in range(self.dim):
            strength = self.resonance_strength[i]
            noise = self.noise_intensity[i]
            freq = self.resonance_freq[i]
            
            # Multiplicative noise resonance
            noise_val = np.random.normal(0, noise)
            resonance_val = strength * np.sin(freq * x[i] + noise_val)
            resonance_component += resonance_val
            
        # Quantum tunneling component for basin hopping
        tunnel_component = 0.0
        for i in range(self.dim):
            prob = self.tunnel_prob[i]
            distance = self.tunnel_distance[i]
            
            # Tunneling probability with distance dependence
            tunnel_val = prob * np.exp(-distance * np.abs(x[i]))
            tunnel_component += tunnel_val
            
        # Coupling between dimensions
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_matrix[i, j] * x[i] * x[j]
                    
        # Nonlinear transformation component
        nonlin_component = 0.0
        for i in range(self.dim):
            power = self.nonlin_power[i]
            shift = self.nonlin_shift[i]
            
            # Nonlinear transformation with power law
            nonlin_val = (x[i] + shift)**power
            nonlin_component += nonlin_val
            
        # Fractal modulation with quantum interference
        fractal_component = 0.0
        for i in range(self.dim):
            scale = self.fractal_scale[i]
            freq = self.fractal_freq[i]
            interference = self.interference_strength[i]
            
            # Fractal-like modulation with interference effects
            fractal_val = scale * np.sin(freq * x[i]) * np.cos(interference * x[i])
            fractal_component += fractal_val
            
        # Combined fitness function
        return (1.5 * quantum_component + 
                1.2 * rbf_component + 
                1.0 * resonance_component + 
                0.8 * tunnel_component + 
                0.6 * coupling_component + 
                0.4 * nonlin_component + 
                0.3 * fractal_component)