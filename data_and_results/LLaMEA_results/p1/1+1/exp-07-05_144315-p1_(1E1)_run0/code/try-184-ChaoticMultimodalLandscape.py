import numpy as np

class ChaoticMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameter initialization
        self.chaos_params = np.sin(np.linspace(0, 2*np.pi, dim)) * 2.0 + 1.0
        self.frequency_modulators = np.log(np.linspace(1.1, 3.0, dim)) + 1.0
        self.amplitude_modulators = np.exp(-np.linspace(0, 2, dim)) + 0.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic polynomial component with dynamic exponents
        chaotic_poly = 0.0
        for i in range(self.dim):
            exponent = 2.0 + 1.5 * np.sin(self.chaos_params[i] * x[i])
            chaotic_poly += (x[i] ** exponent) * (1.0 + 0.3 * np.sin(i * 1.2))
        
        # Hyperbolic tangent exponential component
        tanh_exp = 0.0
        for i in range(self.dim):
            rate = 0.2 + 0.8 * np.cos(i * 0.7)
            tanh_exp += np.tanh(x[i]) * np.exp(-rate * np.abs(x[i]))
        
        # Dynamic sinusoidal with chaotic frequency coupling
        dynamic_sin = 0.0
        for i in range(self.dim):
            freq = self.frequency_modulators[i] * (1.0 + 0.5 * np.sin(x[(i+1) % self.dim]))
            amp = self.amplitude_modulators[i] * (1.0 + 0.2 * np.cos(x[i] * 0.3))
            dynamic_sin += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8)
        
        # Entropy-based valley component with adaptive steepness
        entropy_valley = 0.0
        for i in range(self.dim):
            # Calculate local entropy
            local_entropy = np.abs(x[i]) * np.log(np.abs(x[i]) + 1.0) if x[i] != 0 else 0.0
            steepness = 1.0 + 0.8 * np.tanh(local_entropy)
            if x[i] >= 0:
                entropy_valley += (x[i] ** 2.5) * steepness
            else:
                entropy_valley += (x[i] ** 3.5) * steepness
        
        # Cross-dimensional chaotic interaction with mutual coupling
        cross_chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mutual_coupling = np.sin(x[i] * x[j] * self.chaos_params[i]) * np.cos(x[i] * x[j] * self.chaos_params[j])
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_chaos += mutual_coupling * np.exp(-0.15 * dist)
        
        # Multi-peak landscape with chaotic peak positions and dynamic heights
        multi_peaks = 0.0
        peak_positions = np.sin(np.linspace(0, 4*np.pi, 11)) * 4.0
        for pos in peak_positions:
            width = 0.5 + 0.5 * np.cos(pos * 0.4)
            height = 1.5 + 0.5 * np.sin(pos * 0.6)
            multi_peaks += height * np.exp(-0.5 * np.sum(((x - pos) / width) ** 2))
        
        # Fractional entropy and logarithmic chaos
        entropy_log = 0.0
        for i in range(self.dim):
            if x[i] != 0:
                entropy_log += (np.abs(x[i]) ** 1.8) * np.log(np.abs(x[i]) + 1.0) * np.sin(x[i] * 0.5)
        
        # Combine all components with chaotic weights
        chaotic_weights = np.abs(np.sin(np.linspace(0, 3*np.pi, 6))) + 0.5
        components = np.array([chaotic_poly, tanh_exp, dynamic_sin, entropy_valley, cross_chaos, multi_peaks])
        return np.sum(chaotic_weights * components) + entropy_log