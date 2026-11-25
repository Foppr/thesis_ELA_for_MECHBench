import numpy as np

class QuantumHarmonicRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters with superposition states
        self.oscillator_freq = np.random.uniform(0.5, 3.0, size=dim)
        self.oscillator_amp = np.random.uniform(0.1, 2.0, size=dim)
        self.oscillator_phase = np.random.uniform(0, 2*np.pi, size=dim)
        self.quantum_superposition = np.random.uniform(0.5, 2.0, size=dim)
        
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(15, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=15)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, size=15)
        
        # Dynamic gradient field parameters
        self.gradient_magnitude = np.random.uniform(0.5, 3.0, size=dim)
        self.gradient_decay = np.random.uniform(0.1, 0.8, size=dim)
        self.gradient_directions = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        
        # Time-varying parameters for dynamic landscape
        self.time_freq = np.random.uniform(0.1, 1.0, size=dim)
        self.time_amp = np.random.uniform(0.1, 1.5, size=dim)
        self.time_phase = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Coupling coefficients between dimensions
        self.dimension_coupling = np.random.uniform(-0.5, 0.5, size=(dim, dim))
        np.fill_diagonal(self.dimension_coupling, 0.0)
        
        # Non-linear transformation parameters
        self.nonlinear_power = np.random.uniform(1.5, 4.0, size=dim)
        self.nonlinear_shift = np.random.uniform(-1.0, 1.0, size=dim)
        
        # Multi-scale harmonic components with varying amplitudes
        self.harmonic_freqs = np.random.uniform(1.0, 10.0, size=dim)
        self.harmonic_amps = np.random.uniform(0.2, 1.5, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator component
        quantum_component = 0.0
        for i in range(self.dim):
            oscillator_val = self.oscillator_amp[i] * np.sin(self.oscillator_freq[i] * x[i] + self.oscillator_phase[i])
            quantum_component += self.quantum_superposition[i] * oscillator_val
        
        # Radial basis function component
        rbf_component = 0.0
        for i in range(15):
            dist = np.sum((x - self.rbf_centers[i]) ** 2)
            rbf_val = self.rbf_weights[i] * np.exp(-dist / (2 * self.rbf_widths[i]**2))
            rbf_component += rbf_val
        
        # Dynamic gradient field component
        grad_component = 0.0
        for i in range(self.dim):
            grad_val = 0.0
            for j in range(self.dim):
                if i != j:
                    grad_val += self.dimension_coupling[i, j] * x[j]
            grad_component += self.gradient_magnitude[i] * np.tanh(grad_val) * np.exp(-self.gradient_decay[i] * np.abs(x[i]))
        
        # Time-varying dynamic component
        time_component = 0.0
        for i in range(self.dim):
            time_val = self.time_amp[i] * np.sin(self.time_freq[i] * x[i] + self.time_phase[i])
            time_component += time_val
        
        # Non-linear transformation component
        nonlinear_component = 0.0
        for i in range(self.dim):
            nonlinear_val = (x[i] + self.nonlinear_shift[i]) ** self.nonlinear_power[i]
            nonlinear_component += nonlinear_val
        
        # Multi-scale harmonic component
        harmonic_component = 0.0
        for i in range(self.dim):
            harmonic_val = self.harmonic_amps[i] * np.sin(self.harmonic_freqs[i] * x[i])
            harmonic_component += harmonic_val
        
        # Combined fitness function with balanced weights
        return (1.2 * quantum_component + 
                1.5 * rbf_component + 
                0.8 * grad_component + 
                0.6 * time_component + 
                0.4 * nonlinear_component + 
                0.3 * harmonic_component)