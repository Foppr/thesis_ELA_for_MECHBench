import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced hyperchaotic fractal component with increased nesting and complexity
        fractal = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            scale = 1.0
            nested_sum = 0.0
            for k in range(1, 20):  # Increased nesting to 19 levels
                scale *= 0.28  # Further reduced scaling factor
                nested_sum += scale * np.sin(2**(k+5) * xi + k * np.pi/6)
            fractal += nested_sum
        
        # Enhanced time-delayed feedback with quantum-like phase interactions
        feedback = 0.0
        for i in range(self.dim):
            if i > 2:
                delay = x_norm[i-1] + 0.35 * x_norm[i-2] - 0.25 * x_norm[i-3]
                # Quantum phase interference added with modified coefficients
                phase = np.exp(1j * (14.0 * delay + 0.7 * i))
                feedback += np.real(phase * np.exp(-0.6 * delay**2))
            else:
                feedback += np.sin(14.0 * x_norm[i]) * np.exp(-0.6 * x_norm[i]**2)
        
        # Advanced adaptive landscape erosion with fractal roughness
        erosion = 0.0
        for i in range(self.dim):
            erosion_rate = 0.3 + 0.7 * np.sin(5.0 * x_norm[i]) + 0.4 * np.cos(4.0 * i)
            erosion += erosion_rate * (x_norm[i]**5 - 4.0 * x_norm[i]**3 + 2.0 * x_norm[i])
        
        # Quantum-inspired interference patterns with dynamic frequency modulation
        interference = 0.0
        for i in range(self.dim):
            freq_base = 2.0**(i % 7 + 4)  # Increased base frequency variation
            # Added quantum tunneling effect with different parameters
            tunneling = np.exp(-0.35 * (x_norm[i] - 0.35)**2)
            interference += tunneling * np.sin(freq_base * x_norm[i]) * np.cos(freq_base * x_norm[i] * 1.6)
        
        # Enhanced cross-dimensional coupling with quantum entanglement effects
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Increased coupling range to 7 dimensions
                dist = np.abs(x_norm[i] - x_norm[j])
                # Quantum entanglement strength with different modulation
                entanglement = 0.8 + 0.2 * np.sin(0.7 * (i + j))
                strength = entanglement * np.exp(-dist**2 * (4.0 + 0.7 * (i+j)))
                cross += strength * np.sin(25.0 * dist) * np.cos(10.0 * dist)
        
        # Quantum-inspired dynamic scaling with dimensionality-dependent modulation
        dynamic_scale = 1.0 + 1.0 * np.sin(self.dim * 0.7) * np.cos(np.mean(x_norm)**5)
        
        # Combined components with adjusted weights for improved balance and challenge
        weight_fractal = 0.5 + 0.1 * np.sin(self.dim * 0.4)
        weight_feedback = 0.3 + 0.2 * np.cos(self.dim * 0.35)
        weight_erosion = 0.25 + 0.15 * np.tanh(self.dim * 0.15)
        weight_interference = 0.2 + 0.08 * np.sin(self.dim * 0.3)
        weight_cross = 0.18  # Slightly increased cross-weight for enhanced challenge
        
        return dynamic_scale * (weight_fractal * fractal + 
                               weight_feedback * feedback + 
                               weight_erosion * erosion + 
                               weight_interference * interference + 
                               weight_cross * cross)