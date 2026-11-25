import numpy as np

class QuantumMorphologicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quantum phase factors and morphological structuring elements
        self.phase_factors = np.random.rand(min(15, dim)) * 2 * np.pi
        self.struct_elements = [np.ones((min(3, i+1), min(3, i+1))) for i in range(min(15, dim))]
        self.noise_levels = np.random.rand(min(15, dim)) * 0.5 + 0.1
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum interference component with complex amplitude modulation
        quantum_interference = 0.0
        for i in range(self.dim):
            # Create quantum-like probability amplitudes using sinusoidal modulation
            amp = np.sin(self.phase_factors[i] * x[i]) + 0.5 * np.cos(2 * self.phase_factors[i] * x[i])
            phase = np.exp(1j * x[i] * (i + 1))  # Complex phase evolution
            quantum_interference += np.abs(amp)**2 * np.real(phase)
        
        # Adaptive morphological operations with dynamic structuring elements
        morphological_term = 0.0
        for i in range(self.dim):
            # Apply opening and closing operations with varying structuring element sizes
            elem = self.struct_elements[i % len(self.struct_elements)]
            # Simple morphological opening approximation using local minima
            morph_val = np.min([x[max(0, i-1):min(self.dim, i+2)]]) if i < self.dim - 1 else x[i]
            morphological_term += morph_val * (1 + 0.3 * np.sin(i * 0.5))
        
        # Dynamic basin attraction with time-varying potential wells
        basin_attraction = 0.0
        for i in range(self.dim):
            # Create a multi-well potential landscape with varying depths and positions
            well_depths = np.random.rand(3) * 2 + 1
            well_positions = np.random.rand(3) * 10 - 5
            attraction = 0.0
            for j in range(len(well_depths)):
                dist = (x[i] - well_positions[j])**2
                attraction += well_depths[j] * np.exp(-dist / 4.0)
            basin_attraction += attraction
        
        # Noise sensitivity component with fractal scaling
        noise_sensitivity = 0.0
        for i in range(self.dim):
            # Add noise term that scales with dimensionality and position
            noise_level = self.noise_levels[i % len(self.noise_levels)]
            noise_sensitivity += noise_level * np.sin(x[i] * (i + 1)) * np.cos(x[i]**2)
        
        # Cross-dimensional coupling with quantum entanglement-like interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Simulate quantum correlation between dimensions
                correlation = np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(x[i] + x[j])
                cross_coupling += correlation * (i + j + 1)
        
        # Fractal dimensionality scaling with self-similar landscape features
        fractal_scaling = 0.0
        for i in range(self.dim):
            # Apply fractal-like scaling using fractional Brownian motion characteristics
            fractal_val = np.sin(x[i] * (i + 1)) * np.cos(x[i]**1.5) + \
                         0.5 * np.sin(2 * x[i]) * np.cos(3 * x[i])
            fractal_scaling += fractal_val * (1 + 0.2 * np.sin(i * 0.7))
        
        # Combine all components with optimized weights
        result = 0.7 * quantum_interference + 0.6 * morphological_term + \
                 0.8 * basin_attraction + 0.5 * noise_sensitivity + \
                 0.4 * cross_coupling + 0.6 * fractal_scaling
        
        return result