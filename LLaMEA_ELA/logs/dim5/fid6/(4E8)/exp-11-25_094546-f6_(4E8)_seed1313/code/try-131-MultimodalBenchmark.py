import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis function with quantum-inspired modulation
        rbf = 0.0
        for i in range(self.dim):
            width = 0.4 + 0.3 * np.sin(i * 0.7 + np.pi/4)
            amplitude = 1.2 + 0.6 * np.cos(i * 0.5 + np.pi/3)
            # Add quantum interference term
            interference = 0.3 * np.sin(x_norm[i] * (i + 1) * 2.0)
            rbf += amplitude * np.exp(-0.5 * (x_norm[i] / width)**2) * (1.0 + interference)
        
        # Adaptive harmonic potential with fractal scaling
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.5 + 3.0 * np.sin(i * 0.6 + np.pi/6)
            # Add fractal dimensionality modulation
            fractal_mod = 1.0 + 0.3 * np.sin(i * 0.4 + np.pi/2) * np.cos(i * 0.3)
            harmonic += 0.5 * freq * fractal_mod * (x_norm[i]**2 - 2.0 * x_norm[i] * np.sin(freq * x_norm[i]))
        
        # Enhanced stochastic noise with quantum tunneling effect
        noise = 0.0
        for i in range(self.dim):
            noise_intensity = 0.15 + 0.08 * np.sin(i * 0.8 + np.pi/4)
            # Add quantum tunneling probability
            tunneling_prob = 0.1 * np.cos(x_norm[i] * (i + 1))
            noise += noise_intensity * (np.random.normal(0, 1) + tunneling_prob)
        
        # Cross-dimensional coupling with hyperchaotic interaction
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                # Add hyperchaotic coupling strength
                coupling_strength = 0.4 + 0.3 * np.sin((i+j) * 0.6 + np.pi/3)
                # Add cross-scale energy coupling
                energy_coupling = np.exp(-dist**2 * (1.5 + 0.3 * np.sin(i * 0.5)))
                cross += coupling_strength * energy_coupling
        
        # Dimensionality-dependent scaling with adaptive curvature
        scale_factor = 1.2 + 0.3 * np.sin(self.dim * 0.4 + np.pi/4)
        
        # Dynamic weights with quantum probability distribution
        weight_rbf = 0.35 + 0.1 * np.sin(self.dim * 0.3 + np.pi/6)
        weight_harmonic = 0.3 + 0.2 * np.cos(self.dim * 0.2 + np.pi/3)
        weight_noise = 0.25 + 0.08 * np.tanh(self.dim * 0.15 + np.pi/2)
        weight_cross = 0.1
        
        # Add quantum interference between components
        quantum_phase = 0.1 * np.sin(self.dim * 0.5 + np.pi/4)
        
        return scale_factor * (weight_rbf * rbf + 
                              weight_harmonic * harmonic + 
                              weight_noise * noise + 
                              weight_cross * cross + 
                              quantum_phase * np.sin(np.sum(x_norm)))