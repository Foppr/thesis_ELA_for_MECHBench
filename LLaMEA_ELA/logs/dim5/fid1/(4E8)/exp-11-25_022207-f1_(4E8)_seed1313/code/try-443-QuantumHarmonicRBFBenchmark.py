import numpy as np

class QuantumHarmonicRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters
        self.oscillator_frequencies = np.random.uniform(0.5, 3.0, dim)
        self.oscillator_phases = np.random.uniform(0, 2*np.pi, dim)
        self.oscillator_amplitudes = np.random.uniform(0.5, 2.0, dim)
        # Radial basis function cluster centers and widths
        self.rbf_centers = np.random.uniform(-3.0, 3.0, (15, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.5, 15)
        # Adaptive gradient field parameters
        self.gradient_magnitudes = np.random.uniform(0.1, 1.5, dim)
        self.gradient_directions = np.random.randn(dim, dim)
        self.gradient_directions = self.gradient_directions / np.linalg.norm(self.gradient_directions, axis=1, keepdims=True)
        # Entropic conditioning parameters
        self.entropic_factors = np.random.uniform(0.5, 2.0, dim)
        self.entropic_exponents = np.random.uniform(1.0, 3.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Quantum harmonic oscillator terms
        quantum_term = 0.0
        for i in range(self.dim):
            freq = self.oscillator_frequencies[i]
            phase = self.oscillator_phases[i]
            amp = self.oscillator_amplitudes[i]
            # Quantum harmonic potential
            quantum_val = amp * (freq * x_norm[i] + phase)**2 + np.sin(freq * x_norm[i] + phase)
            quantum_term += quantum_val
            
        # Radial basis function clustering
        rbf_term = 0.0
        for i in range(15):  # 15 RBF centers
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            # Gaussian RBF with adaptive width
            distance = np.linalg.norm(x_norm - center)
            rbf_val = np.exp(-0.5 * (distance / width)**2)
            rbf_term += rbf_val
            
        # Adaptive gradient field
        grad_term = 0.0
        for i in range(self.dim):
            mag = self.gradient_magnitudes[i]
            direction = self.gradient_directions[i]
            # Gradient field with directional influence
            grad_val = mag * np.dot(x_norm, direction)
            grad_term += grad_val
            
        # Entropic conditioning
        entropic_term = 0.0
        for i in range(self.dim):
            factor = self.entropic_factors[i]
            exponent = self.entropic_exponents[i]
            # Entropic penalty with adaptive exponent
            entropic_val = factor * (np.abs(x_norm[i]) ** exponent)
            entropic_term += entropic_val
            
        # Combined function with weighted components
        result = 1.2 * quantum_term + 0.8 * rbf_term + 1.0 * grad_term + 0.6 * entropic_term
        
        # Add quantum noise with entropic characteristics
        noise_amplitude = 0.02 * (1.0 + 0.05 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise