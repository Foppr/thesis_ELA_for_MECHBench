import numpy as np

class ExponentialResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic exponential decay potentials with chaotic exponents
        self.decay_exponents = np.random.rand(dim) * 5.0 + 2.0
        # Quantum harmonic resonance frequencies with chaotic modulation
        self.resonance_freqs = np.random.rand(dim) * 15.0 + 10.0
        # Adaptive elliptic shaping with dynamic axes
        self.elliptic_axes = np.random.rand(dim) * 3.0 + 2.0
        self.elliptic_angles = np.random.rand(dim) * np.pi * 2
        # Dynamic conditioning factors
        self.conditioning_factors = np.random.rand(dim) * 6.0 + 2.0
        # Cross-dimensional coupling with chaotic strengths
        self.coupling_strengths = np.random.rand(dim, dim) * 1.2 + 0.5
        # Dynamic phase shift parameters
        self.phase_shifts = np.random.rand(dim) * 4.0 * np.pi
        # Quartic nonlinearities for increased complexity
        self.quartic_coefficients = np.random.rand(dim) * 0.8 + 0.3
        # Chaotic modulation factors
        self.modulation_factors = np.random.rand(dim) * 2.0 + 1.0
        # Additional chaotic sine-wave components for enhanced multimodality
        self.sine_amplitudes = np.random.rand(dim) * 3.0 + 1.0
        self.sine_frequencies = np.random.rand(dim) * 8.0 + 4.0
        # Saddle-point complexity enhancement
        self.saddle_strengths = np.random.rand(dim) * 2.0 + 1.0
        # Novel chaotic hyperbolic tangent components for increased complexity
        self.tanh_amplitudes = np.random.rand(dim) * 2.0 + 1.0
        self.tanh_coefficients = np.random.rand(dim) * 3.0 + 1.0
        # Fractal-like dimensionality scaling factors
        self.fractal_scaling = np.random.rand(dim) * 0.5 + 0.25
        # Enhanced cross-dimensional coupling with fractal interactions
        self.fractal_coupling = np.random.rand(dim, dim) * 2.0 + 1.0
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic exponential decay potential component
        exp_potential = 0.0
        for i in range(self.dim):
            exp_potential += np.exp(-self.decay_exponents[i] * np.abs(x_norm[i])) * \
                           np.sin(self.modulation_factors[i] * x_norm[i])
            
        # Quantum harmonic resonance component with dynamic phase shifts
        harmonic_resonance = 0.0
        for i in range(self.dim):
            freq = self.resonance_freqs[i]
            phase = self.phase_shifts[i]
            harmonic_resonance += np.sin(freq * x_norm[i] + phase) * \
                                np.cos(freq * x_norm[i] + phase) * \
                                np.exp(-0.1 * np.abs(x_norm[i]))
                                
        # Elliptic shaping component with dynamic rotation
        elliptic_shaping = 0.0
        for i in range(self.dim):
            a = self.elliptic_axes[i]
            angle = self.elliptic_angles[i]
            x_rot = x_norm[i] * np.cos(angle) - x_norm[(i+1) % self.dim] * np.sin(angle)
            y_rot = x_norm[i] * np.sin(angle) + x_norm[(i+1) % self.dim] * np.cos(angle)
            elliptic_shaping += (x_rot**2 / a**2 + y_rot**2) * 0.5
            
        # Adaptive conditioning with chaotic modulation
        adaptive_conditioning = 0.0
        for i in range(self.dim):
            adaptive_conditioning += self.conditioning_factors[i] * x_norm[i]**2 * \
                                  np.cos(0.5 * x_norm[i])
            
        # Cross-dimensional coupling with chaotic interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_coupling += self.coupling_strengths[i, j] * x_norm[i] * x_norm[j] * \
                                    np.sin(0.3 * (x_norm[i] + x_norm[j]))
                    
        # Quartic nonlinearities with chaotic modulation
        quartic_nonlinearities = 0.0
        for i in range(self.dim):
            quartic_nonlinearities += self.quartic_coefficients[i] * x_norm[i]**4 * \
                                    np.cos(0.2 * x_norm[i])
        
        # Additional sine-wave components for enhanced multimodality
        sine_components = 0.0
        for i in range(self.dim):
            sine_components += self.sine_amplitudes[i] * np.sin(self.sine_frequencies[i] * x_norm[i]) * \
                              np.cos(0.1 * x_norm[i]**2)
        
        # Saddle-point complexity enhancement
        saddle_points = 0.0
        for i in range(self.dim):
            saddle_points += self.saddle_strengths[i] * x_norm[i]**3 * np.sin(x_norm[i])
            
        # Novel chaotic hyperbolic tangent components
        tanh_components = 0.0
        for i in range(self.dim):
            tanh_components += self.tanh_amplitudes[i] * np.tanh(self.tanh_coefficients[i] * x_norm[i]) * \
                              np.exp(-0.2 * x_norm[i]**2)
        
        # Fractal-like dimensionality scaling
        fractal_scaling = 0.0
        for i in range(self.dim):
            fractal_scaling += self.fractal_scaling[i] * np.sin(x_norm[i]**3) * \
                              np.cos(x_norm[i]**2)
        
        # Enhanced cross-dimensional coupling with fractal interactions
        fractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    fractal_coupling += self.fractal_coupling[i, j] * x_norm[i] * x_norm[j] * \
                                      np.tanh(0.5 * (x_norm[i] + x_norm[j]))
        
        # Combined function with multiple chaotic interaction terms
        return (3.0 * exp_potential + 2.0 * harmonic_resonance + 1.2 * elliptic_shaping + 
                0.5 * adaptive_conditioning + 0.4 * cross_coupling + 0.3 * quartic_nonlinearities +
                0.2 * sine_components + 0.1 * saddle_points + 0.15 * tanh_components + 
                0.1 * fractal_scaling + 0.05 * fractal_coupling + 2.0)